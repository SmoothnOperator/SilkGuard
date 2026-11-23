import os
import win32com.client

def apply_animations_to_deck():
    src_pptx = r"C:\Users\NIKHI\Downloads\SilkGuard Intelligent Leaf Scanning & Sericulture Protection Platform.pptx"
    out_animated = r"C:\Users\NIKHI\Downloads\SilkGuard Intelligent Leaf Scanning & Sericulture Protection Platform (Animated).pptx"
    out_workspace = r"d:\code\leaf\EXP\SilkGuard_Faculty_Presentation_Animated.pptx"

    if not os.path.exists(src_pptx):
        print("Source file not found:", src_pptx)
        return

    print("Opening PowerPoint application...")
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    ppt_app.Visible = True

    pres = ppt_app.Presentations.Open(src_pptx, WithWindow=False)
    total_slides = pres.Slides.Count
    print(f"Loaded presentation with {total_slides} slides.")

    # Animation & Transition Constants
    ppEffectFade = 769          # Smooth fade slide transition
    ppEffectPushRight = 1282     # Push right transition (alternative)
    msoAnimEffectFade = 10      # Fade entrance effect
    msoAnimEffectFloat = 42     # Float entrance effect
    msoAnimEffectFly = 2        # Fly entrance effect
    msoAnimTriggerAfterPrevious = 3
    msoAnimTriggerWithPrevious = 2
    msoAnimTriggerOnPageClick = 1

    for s_idx in range(1, total_slides + 1):
        slide = pres.Slides(s_idx)
        seq = slide.TimeLine.MainSequence

        # 1. Apply Slide Transition to EVERY slide
        slide.SlideShowTransition.EntryEffect = ppEffectFade
        slide.SlideShowTransition.Duration = 0.45
        slide.SlideShowTransition.AdvanceOnClick = True

        # Clear any existing timeline effects
        while seq.Count > 0:
            seq(1).Delete()

        # Separate Shapes by Role
        content_shapes = []
        header_shapes = []
        footer_shapes = []

        for j in range(1, slide.Shapes.Count + 1):
            sp = slide.Shapes(j)
            # Footer: at the bottom of the slide
            if sp.Top >= 475:
                footer_shapes.append(sp)
            # Header: Top logo or section tracker / slide title
            elif (sp.Top < 50 and sp.Left > 600) or (sp.Top < 125 and s_idx > 1):
                header_shapes.append(sp)
            else:
                content_shapes.append(sp)

        # Slide 1 (Title Slide) Custom Staggered Animation
        if s_idx == 1:
            # Shape order: Logo, Category tracker, Title, Gold bar, Subtitle, Dept, Guide
            # Animate all content sequentially with smooth fade
            for idx, sp in enumerate(content_shapes):
                eff = seq.AddEffect(sp, msoAnimEffectFloat if idx in [1, 2, 4] else msoAnimEffectFade, 0, msoAnimTriggerAfterPrevious)
                eff.Timing.Duration = 0.4
                eff.Timing.TriggerDelayTime = 0.12
            print(f"Slide 01: Animated {len(content_shapes)} title components.")
            continue

        # For Content Slides (Slides 2 to 26):
        # Header title gentle entrance
        if len(header_shapes) >= 2:
            # Shape 2 is category, Shape 3 is Title
            # Fade in title with previous right as slide starts
            eff_title = seq.AddEffect(header_shapes[-1], msoAnimEffectFade, 0, msoAnimTriggerWithPrevious)
            eff_title.Timing.Duration = 0.3
            eff_title.Timing.TriggerDelayTime = 0.05

        # Group Content Shapes into Logical Cards/Units
        # A) Detect background panel/card containers (AutoShapes with empty text and area > 9000)
        containers = []
        for sp in content_shapes:
            has_no_text = (not sp.HasTextFrame) or (sp.TextFrame.TextRange.Text.strip() == "")
            if has_no_text and (sp.Width * sp.Height > 9000) and sp.Type in [1, 5, 6]:
                containers.append(sp)

        groups = []
        assigned = set()

        # Assign child elements inside each container
        for c in containers:
            grp = [c]
            assigned.add(c.Id)
            cx1, cy1, cx2, cy2 = c.Left - 5, c.Top - 5, c.Left + c.Width + 5, c.Top + c.Height + 5
            for sp in content_shapes:
                if sp.Id not in assigned:
                    scx = sp.Left + sp.Width / 2.0
                    scy = sp.Top + sp.Height / 2.0
                    if cx1 <= scx <= cx2 and cy1 <= scy <= cy2:
                        grp.append(sp)
                        assigned.add(sp.Id)
            groups.append(grp)

        # Remaining shapes that were not inside any container card
        remaining = [sp for sp in content_shapes if sp.Id not in assigned]

        # If there are many loose shapes (e.g. matrix or charts like slide 15, 5, 11, 17)
        if len(remaining) > 8:
            # Cluster remaining shapes by column (Left < 450 vs Left >= 450) and bottom note
            col_left = []
            col_right = []
            bottom_notes = []
            for sp in remaining:
                if sp.Top > 400:
                    bottom_notes.append(sp)
                elif sp.Left < 450:
                    col_left.append(sp)
                else:
                    col_right.append(sp)

            if col_left:
                groups.append(col_left)
            if col_right:
                groups.append(col_right)
            if bottom_notes:
                groups.append(bottom_notes)
        else:
            for sp in remaining:
                groups.append([sp])

        # Sort groups in reading order (Top to Bottom, Left to Right)
        groups.sort(key=lambda g: (round(g[0].Top / 30.0) * 30.0, g[0].Left))

        # Add Animation Effects to Groups
        for g_idx, grp in enumerate(groups):
            # First shape in the group triggers AfterPrevious (cascading entrance)
            first_sp = grp[0]
            eff_lead = seq.AddEffect(first_sp, msoAnimEffectFloat if first_sp.Type in [1, 5] else msoAnimEffectFade, 0, msoAnimTriggerAfterPrevious)
            eff_lead.Timing.Duration = 0.35
            eff_lead.Timing.TriggerDelayTime = 0.15

            # Subsequent shapes inside the SAME card appear WithPrevious so the card appears unified
            for inner_sp in grp[1:]:
                eff_inner = seq.AddEffect(inner_sp, msoAnimEffectFade, 0, msoAnimTriggerWithPrevious)
                eff_inner.Timing.Duration = 0.3
                eff_inner.Timing.TriggerDelayTime = 0.05

        print(f"Slide {s_idx:02d}: Added transition + animations across {len(groups)} content groups ({seq.Count} effects).")

    # Save to both locations
    print(f"Saving animated presentation to: {out_animated}")
    pres.SaveAs(out_animated)

    print(f"Saving animated presentation copy to workspace: {out_workspace}")
    pres.SaveAs(out_workspace)

    # Overwrite the original downloaded file so when user opens it directly, it has animations!
    print(f"Updating original file in-place: {src_pptx}")
    pres.SaveAs(src_pptx)

    pres.Close()
    ppt_app.Quit()
    print("All animations successfully applied to every slide!")

if __name__ == "__main__":
    apply_animations_to_deck()
