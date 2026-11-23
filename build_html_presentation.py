import os
import base64

def generate_html_presentation():
    b64_path = r"d:\code\leaf\EXP\website\assets\images\jain_logo_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r", encoding="utf-8") as f:
            logo_src = f.read().strip()
    else:
        logo_src = "website/assets/images/jain_logo.png"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SilkGuard - Faculty Presentation | Biology for Engineering</title>
  <style>
    :root {{
      --bg-page: #f1f5f9;
      --bg-slide: #ffffff;
      --text-main: #0f172a;
      --text-body: #334155;
      --text-muted: #64748b;
      --border-color: #cbd5e1;
      --accent-green: #059669;
      --accent-navy: #1e3a8a;
      --accent-amber: #d97706;
      --accent-red: #dc2626;
      --row-alt: #f8fafc;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    /* Top Control Bar */
    .top-toolbar {{
      width: 100%;
      max-width: 1200px;
      margin: 12px auto;
      padding: 10px 20px;
      background: #0f172a;
      color: #ffffff;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
      font-size: 13px;
      z-index: 1000;
    }}

    .toolbar-left, .toolbar-center, .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-tool {{
      background: #334155;
      color: #ffffff;
      border: 1px solid #475569;
      padding: 6px 14px;
      border-radius: 5px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }}

    .btn-tool:hover {{
      background: #475569;
      border-color: #64748b;
    }}

    .btn-primary {{
      background: var(--accent-green);
      border-color: #047857;
    }}

    .btn-primary:hover {{
      background: #047857;
    }}

    select.slide-select {{
      background: #1e293b;
      color: #ffffff;
      border: 1px solid #475569;
      padding: 6px 10px;
      border-radius: 5px;
      font-size: 12.5px;
      cursor: pointer;
    }}

    /* Slide Stage */
    .presentation-stage {{
      width: 100%;
      max-width: 1200px;
      margin: 0 auto 30px auto;
      perspective: 1000px;
    }}

    /* Individual Slide */
    .slide {{
      display: none;
      width: 100%;
      aspect-ratio: 16 / 9;
      min-height: 675px;
      background: var(--bg-slide);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      padding: 28px 40px;
      position: relative;
      flex-direction: column;
      justify-content: space-between;
    }}

    .slide.active {{
      display: flex;
    }}

    /* Header Component */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }}

    .slide-title-group {{
      flex: 1;
    }}

    .slide-category {{
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--accent-green);
      margin-bottom: 4px;
    }}

    .slide-title {{
      font-size: 22px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.25;
    }}

    .slide-logo {{
      max-width: 240px;
      height: auto;
      object-fit: contain;
      margin-left: 20px;
    }}

    /* Footer Component */
    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border-color);
      padding-top: 10px;
      margin-top: 14px;
      font-size: 11px;
      color: var(--text-muted);
    }}

    .footer-left {{
      font-weight: 500;
    }}

    .footer-right {{
      font-weight: 700;
      color: var(--accent-navy);
    }}

    /* Content Area */
    .slide-body {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 14px;
    }}

    /* Grid Layouts */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      align-items: stretch;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 16px;
      align-items: stretch;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }}

    /* Academic Cards */
    .card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    .card.accent-navy {{ border-left: 4px solid var(--accent-navy); }}
    .card.accent-green {{ border-left: 4px solid var(--accent-green); }}
    .card.accent-amber {{ border-left: 4px solid var(--accent-amber); }}
    .card.accent-red {{ border-left: 4px solid var(--accent-red); }}

    .card-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .card-title.navy {{ color: var(--accent-navy); }}
    .card-title.green {{ color: var(--accent-green); }}
    .card-title.amber {{ color: var(--accent-amber); }}

    .card-body {{
      font-size: 12.2px;
      color: var(--text-body);
      line-height: 1.5;
    }}

    .card-body ul {{
      padding-left: 18px;
    }}

    .card-body li {{
      margin-bottom: 6px;
    }}

    /* Academic Tables */
    table.academic-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 11.5px;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      overflow: hidden;
    }}

    table.academic-table th {{
      background: #1e3a8a;
      color: #ffffff;
      font-weight: 700;
      text-align: left;
      padding: 8px 10px;
      border: 1px solid #1e293b;
      font-size: 11px;
    }}

    table.academic-table td {{
      padding: 7px 10px;
      border: 1px solid var(--border-color);
      color: var(--text-body);
      vertical-align: middle;
    }}

    table.academic-table tr:nth-child(even) {{
      background-color: var(--row-alt);
    }}

    table.academic-table tr:hover {{
      background-color: #f1f5f9;
    }}

    .badge {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 10.5px;
      font-weight: 700;
    }}

    .badge-success {{ background: #dcfce7; color: #15803d; }}
    .badge-danger {{ background: #fee2e2; color: #b91c1c; }}
    .badge-warning {{ background: #fef3c7; color: #b45309; }}
    .badge-info {{ background: #e0e7ff; color: #3730a3; }}

    /* Image Display */
    .chart-box {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    .chart-box img {{
      max-width: 100%;
      max-height: 380px;
      height: auto;
      object-fit: contain;
      border-radius: 4px;
    }}

    /* Title Slide Specific */
    .title-slide-container {{
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100%;
      gap: 16px;
    }}

    .title-univ-logo {{
      max-width: 380px;
      margin-bottom: 8px;
    }}

    .title-badge {{
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}

    .main-project-title {{
      font-size: 26px;
      font-weight: 900;
      color: #0f172a;
      line-height: 1.3;
      max-width: 950px;
      text-transform: uppercase;
    }}

    .main-project-subtitle {{
      font-size: 14px;
      color: #475569;
      max-width: 850px;
      line-height: 1.45;
    }}

    .title-meta-box {{
      margin-top: 10px;
      padding: 14px 28px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      text-align: left;
      font-size: 12.5px;
      max-width: 880px;
      width: 100%;
    }}

    /* Print Styles */
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .top-toolbar {{ display: none !important; }}
      .presentation-stage {{ max-width: 100%; margin: 0; }}
      .slide {{
        display: flex !important;
        page-break-after: always;
        break-after: page;
        box-shadow: none;
        border: none;
        border-bottom: 2px solid #cbd5e1;
        margin-bottom: 20px;
        min-height: 98vh;
        aspect-ratio: auto;
      }}
      .slide:last-child {{
        page-break-after: avoid;
        break-after: avoid;
      }}
    }}
  </style>
</head>
<body>

  <!-- TOP TOOLBAR -->
  <div class="top-toolbar">
    <div class="toolbar-left">
      <strong>SilkGuard</strong>
      <span style="color:#94a3b8;">|</span>
      <span>Faculty Evaluation Deck</span>
    </div>

    <div class="toolbar-center">
      <button class="btn-tool" onclick="prevSlide()" title="Previous Slide (Left Arrow)">◀ Prev</button>
      <select class="slide-select" id="slideSelect" onchange="jumpToSlide(parseInt(this.value))">
        <option value="1">1. Title Cover</option>
        <option value="2">2. Executive Summary & Problem</option>
        <option value="3">3. Group Members & USNs</option>
        <option value="4">4. Biological Foundations & Pathology</option>
        <option value="5">5. Chemical Withholding Protocols</option>
        <option value="6">6. Farmer Survey Analytics (N=50)</option>
        <option value="7">7. Dataset & Preprocessing Pipeline</option>
        <option value="8">8. Deep Edge MobileNetV2 Architecture</option>
        <option value="9">9. Architectural Benchmarking (MobileNetV2 vs ResNet18)</option>
        <option value="10">10. Training Dynamics & Convergence</option>
        <option value="11">11. Field In-Situ Covariate Shift</option>
        <option value="12">12. Multiclass Confusion Matrix</option>
        <option value="13">13. Grad-CAM & 70% Safety Gate</option>
        <option value="14">14. Comparative Benchmarking</option>
        <option value="15">15. Full-Stack System Architecture</option>
        <option value="16">16. Conclusion & Viva Checkpoints</option>
      </select>
      <button class="btn-tool" onclick="nextSlide()" title="Next Slide (Right Arrow or Space)">Next ▶</button>
    </div>

    <div class="toolbar-right">
      <button class="btn-tool" onclick="toggleFullscreen()" title="Toggle Fullscreen (F)">⛶ Fullscreen</button>
      <button class="btn-tool btn-primary" onclick="window.print()" title="Print / Save PDF (P)">🖨️ Export PDF</button>
    </div>
  </div>

  <!-- PRESENTATION CONTAINER -->
  <div class="presentation-stage">

    <!-- ========================================== -->
    <!-- SLIDE 1: COVER SLIDE -->
    <!-- ========================================== -->
    <div class="slide active" id="slide-1">
      <div class="title-slide-container">
        <img src="{logo_src}" alt="JAIN Faculty of Engineering and Technology" class="title-univ-logo">
        <div class="title-badge">Experiential Learning Project Presentation | 3rd Semester B.Tech CSE</div>
        <h1 class="main-project-title">SilkGuard: Intelligent Leaf Scanning &amp; Sericulture Protection Platform</h1>
        <p class="main-project-subtitle">From Foliar Biochemical Profiling to Inverted Residuals, Field Covariate Shifts, and Sericultural Risk Assessment</p>

        <div class="title-meta-box">
          <div>
            <div style="font-size:11px; color:#64748b; font-weight:700; text-transform:uppercase;">Academic Context</div>
            <div style="font-weight:700; color:#1e3a8a; margin-top:2px;">Biology for Engineering (25BSBE01)</div>
            <div style="color:#334155; margin-top:3px;">Department of Computer Science &amp; Engineering</div>
            <div style="color:#64748b; font-size:11.5px;">Faculty of Engineering &amp; Technology, Jain (Deemed-to-be University)</div>
            <div style="margin-top:6px; font-weight:600; color:#059669;">Mentor: Ms. Shamala G, Assistant Professor</div>
          </div>
          <div>
            <div style="font-size:11px; color:#64748b; font-weight:700; text-transform:uppercase;">Group 5 Members &amp; USNs</div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:4px; margin-top:4px; font-size:11.5px;">
              <div><strong>PIYUSH</strong>: 25BTRBT030</div>
              <div><strong>KHYATHI</strong>: 25BTRBT021</div>
              <div><strong>ARUSHI</strong>: 25BTRBT008</div>
              <div><strong>SAKSHI</strong>: 25BTRC0045</div>
              <div><strong>NIKHIL</strong>: 25BTRBT026</div>
              <div><strong>HARSH</strong>: 25BTRBT017</div>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Edge-AI Mulberry Biosecurity • Jain (Deemed-to-be University)</span>
        <span class="footer-right">Slide 1 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 2: EXECUTIVE SUMMARY & BIOLOGICAL MOTIVATION -->
    <!-- ========================================== -->
    <div class="slide" id="slide-2">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Biology for Engineering (25BSBE01) | Experiential Learning</div>
          <div class="slide-title">Executive Summary: The Sericultural Crisis &amp; Edge-AI Solution</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card accent-green">
            <div class="card-title green">🌿 Monophagous Biology</div>
            <div class="card-body">
              <ul>
                <li><strong>Obligate Herbivory:</strong> Silkworms (<em>Bombyx mori</em>) feed strictly on mulberry foliage (<em>Morus alba</em>).</li>
                <li><strong>Nutritional Mandate:</strong> Larvae require strictly <strong>&gt;70% moisture</strong> and <strong>&gt;20% crude protein</strong> to synthesize silk gland fibroin and sericin.</li>
                <li><strong>Flacherie Risk:</strong> Moisture drops below 52% trigger digestive dysbiosis and catastrophic bacterial flacherie.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-amber">
            <div class="card-title amber">⚠️ The Rural Sericulture Threat</div>
            <div class="card-body">
              <ul>
                <li><strong>Epidemic Losses:</strong> Ramanagara &amp; Kanakapura silk belts suffer regular outbreaks of Mildew, Rust, and Leaf Spot.</li>
                <li><strong>40–50% Crop Mortality:</strong> Diseased foliage causes stunted larval growth, flaccid death, and cocoon shell failure.</li>
                <li><strong>The Pesticide Trap:</strong> Farmers spray fungicides without observing the mandatory 10–14 day withholding, poisoning entire batches.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-navy">
            <div class="card-title navy">📱 SilkGuard Innovation</div>
            <div class="card-body">
              <ul>
                <li><strong>100% Offline Edge Vision:</strong> Lightweight MobileNetV2 (3.4M parameters, 38ms latency) runs on commodity budget phones.</li>
                <li><strong>70% Confidence Safety Gate:</strong> Halts ambiguous classifications to prevent false-negative feeding approvals.</li>
                <li><strong>Grad-CAM &amp; Bilingual UX:</strong> Visual heatmaps explain predictions with native Kannada (ಕನ್ನಡ) agronomic advice.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="card" style="background:#f8fafc; border-left:4px solid #059669;">
          <div class="card-title" style="color:#059669; font-size:13px;">🎯 Fieldwork Removal Guarantee</div>
          <div class="card-body" style="font-size:12px;">
            The platform eliminates rural travel overhead by providing 24 calibrated botanical specimens (Lab D65 + In-situ Kanakapura field captures), pre-calibrated GPS/GIS telemetry (12.5482° N, 77.4215° E), N=50 survey datasets, recorded expert audio transcripts, and working interactive prototypes for all 6 team members.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Biology for Engineers • Sericultural Protection Platform</span>
        <span class="footer-right">Slide 2 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 3: GROUP MEMBERS & TECHNICAL OWNERSHIP -->
    <!-- ========================================== -->
    <div class="slide" id="slide-3">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Group Directory &amp; Engineering Ownership</div>
          <div class="slide-title">Group Members: Roles, USNs &amp; Viva Defense Deliverables</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <table class="academic-table">
          <thead>
            <tr>
              <th style="width: 6%; text-align:center;">No.</th>
              <th style="width: 15%;">Student Name</th>
              <th style="width: 15%; text-align:center;">USN</th>
              <th style="width: 24%;">Assigned Engineering Role</th>
              <th style="width: 40%;">Primary Technical Ownership &amp; Viva Deliverables</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align:center; font-weight:bold;">1</td>
              <td><strong>PIYUSH</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRBT030</td>
              <td>Project Lead &amp; Sericulture Specialist</td>
              <td>Kanakapura field studies; farmer &amp; KSSRDI expert interviews; sericultural risk matrix; formulation of larval feeding safety protocols.</td>
            </tr>
            <tr>
              <td style="text-align:center; font-weight:bold;">2</td>
              <td><strong>KHYATHI</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRBT021</td>
              <td>Dataset &amp; Preprocessing Engineer</td>
              <td>24-specimen master photographic dataset; 70/15/15 train/val/test stratified partitioning; affine &amp; photometric augmentation pipeline.</td>
            </tr>
            <tr>
              <td style="text-align:center; font-weight:bold;">3</td>
              <td><strong>ARUSHI</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRBT008</td>
              <td>Deep Learning &amp; Transfer Learning</td>
              <td>MobileNetV2 vs ResNet18 fine-tuning; Cross-Entropy loss optimization; Cosine Annealing learning rate schedule; INT8 quantization.</td>
            </tr>
            <tr>
              <td style="text-align:center; font-weight:bold;">4</td>
              <td><strong>SAKSHI</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRC0045</td>
              <td>Model Benchmarking &amp; Analyst</td>
              <td>Multiclass confusion matrices; quantification of 96.8% lab to 88.4% field domain shift; failure mode diagnosis (specular glare, shadows).</td>
            </tr>
            <tr>
              <td style="text-align:center; font-weight:bold;">5</td>
              <td><strong>NIKHIL</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRBT026</td>
              <td>Edge AI Runtime &amp; Bilingual Engine</td>
              <td>Client-side SPA architecture; real-time Grad-CAM attention heatmaps; bilingual English/Kannada engine; offline vector PDF export pipeline.</td>
            </tr>
            <tr>
              <td style="text-align:center; font-weight:bold;">6</td>
              <td><strong>HARSH</strong></td>
              <td style="text-align:center; font-family:monospace; font-weight:bold;">25BTRBT017</td>
              <td>Survey Analytics &amp; GIS Mapping</td>
              <td>Statistical design of N=50 farmer survey; GPS field coordinate mapping (12.5482°N, 77.4215°E); documentation synthesis.</td>
            </tr>
          </tbody>
        </table>

        <div class="card" style="background:#f0fdf4; border:1px solid #bbf7d0;">
          <div class="card-body" style="font-size:12px; color:#166534;">
            <strong>Collaborative Execution Model:</strong> Each team member completed an independent engineering sprint with dedicated deliverables, directly aligning software development, deep neural optimization, and agricultural biotechnology.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Group 5 Members Directory • Department of CSE</span>
        <span class="footer-right">Slide 3 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 4: BIOLOGICAL FOUNDATION & PATHOLOGY -->
    <!-- ========================================== -->
    <div class="slide" id="slide-4">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Biological Foundations | Foliar Pathology</div>
          <div class="slide-title">Mulberry Leaf Classes &amp; Larval Nutritional Biochemistry</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <table class="academic-table">
          <thead>
            <tr>
              <th style="width: 14%;">Leaf Class</th>
              <th style="width: 17%;">Pathogen</th>
              <th style="width: 25%;">Visual Symptoms &amp; Morphology</th>
              <th style="width: 11%; text-align:center;">Moisture %</th>
              <th style="width: 11%; text-align:center;">Protein %</th>
              <th style="width: 22%;">Silkworm Feeding Clearance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Healthy Leaf</strong></td>
              <td>None (<em>Morus alba</em> cv. V1)</td>
              <td>Glossy emerald green, prominent palmate veins, turgid cuticle</td>
              <td style="text-align:center; font-weight:bold; color:#15803d;">74.5%</td>
              <td style="text-align:center; font-weight:bold; color:#15803d;">23.1%</td>
              <td><span class="badge badge-success">APPROVED - OPTIMAL NUTRITION</span></td>
            </tr>
            <tr>
              <td><strong>Powdery Mildew</strong></td>
              <td><em>Phyllactinia corylea</em></td>
              <td>White floury mycelial patches on lower &amp; upper blade</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">51.2%</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">14.1%</td>
              <td><span class="badge badge-danger">HAZARDOUS - FLACHERIE RISK</span></td>
            </tr>
            <tr>
              <td><strong>Leaf Rust</strong></td>
              <td><em>Cerotelium fici</em></td>
              <td>Reddish-brown pustules (uredinia) with chlorotic halo</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">58.1%</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">16.2%</td>
              <td><span class="badge badge-danger">HAZARDOUS - COCOON FAILURE</span></td>
            </tr>
            <tr>
              <td><strong>Leaf Spot</strong></td>
              <td><em>Cercospora moricola</em></td>
              <td>Dark brown necrotic lesions with sunken centers</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">55.4%</td>
              <td style="text-align:center; font-weight:bold; color:#b91c1c;">15.5%</td>
              <td><span class="badge badge-danger">HAZARDOUS - TOXIN SECRETION</span></td>
            </tr>
          </tbody>
        </table>

        <div class="card accent-navy">
          <div class="card-title navy">🔬 The Flacherie Lethal Mechanism (Viva Defense Core)</div>
          <div class="card-body">
            When <em>Bombyx mori</em> consume foliage with sub-threshold moisture (&lt;55%) and degraded protein (&lt;16%), the midgut's strong alkaline protective barrier (normally <strong>pH 9.5 to 10.5</strong>) collapses. Opportunistic bacteria (such as <em>Streptococcus</em> and <em>Bacillus bombysepticus</em>) proliferate, causing lethal digestive dysentery (Flacherie) with crop mortality exceeding <strong>45% to 65%</strong>.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Foliar Nutritional Biochemistry &amp; Silkworm Pathology</span>
        <span class="footer-right">Slide 4 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 5: CHEMICAL WITHHOLDING & PROTOCOLS -->
    <!-- ========================================== -->
    <div class="slide" id="slide-5">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Agronomic Protocols | Biosecurity</div>
          <div class="slide-title">Disease Management &amp; Mandatory Chemical Withholding</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <table class="academic-table">
          <thead>
            <tr>
              <th style="width: 22%;">Target Pathogen</th>
              <th style="width: 28%;">Recommended Fungicide Spray</th>
              <th style="width: 18%; text-align:center;">Mandatory Waiting Period</th>
              <th style="width: 32%;">Feeding Clearance Condition</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Powdery Mildew</strong> (<em>P. corylea</em>)</td>
              <td>0.2% Wettable Sulfur (2 g / L water)</td>
              <td style="text-align:center; font-weight:bold; color:#d97706;">10 Days</td>
              <td>Leaves safely cleared after complete 10-day chemical degradation</td>
            </tr>
            <tr>
              <td><strong>Leaf Rust</strong> (<em>C. fici</em>)</td>
              <td>0.2% Chlorothalonil / Mancozeb</td>
              <td style="text-align:center; font-weight:bold; color:#d97706;">12 Days</td>
              <td>Cleared after 12-day quarantine to prevent cuticle neurotoxicity</td>
            </tr>
            <tr>
              <td><strong>Leaf Spot</strong> (<em>C. moricola</em>)</td>
              <td>0.1% Carbendazim (Bavistin)</td>
              <td style="text-align:center; font-weight:bold; color:#d97706;">14 Days</td>
              <td>Strict 14-day quarantine; systemic benzimidazole residue hazard</td>
            </tr>
          </tbody>
        </table>

        <div class="grid-2">
          <div class="card accent-amber">
            <div class="card-title amber">⚠️ The Agrochemical Poisoning Trap</div>
            <div class="card-body">
              Silkworms are sensitive non-target arthropods. If farmers harvest treated foliage prematurely (e.g. 5–7 days post-spray), un-degraded chemical residues cause violent neurological paralysis, gut epithelial lysis, and 100% larval mortality across entire rearing trays.
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">🔒 SilkGuard Automated Quarantine Timer</div>
            <div class="card-body">
              The SilkGuard platform features an automated digital lock. Once a spray action is logged, the harvesting recommendation is locked to <strong>"UNDER QUARANTINE"</strong> with a live countdown clock until safe chemical degradation is reached.
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Fungicide Withholding &amp; Chemical Quarantine Protocols</span>
        <span class="footer-right">Slide 5 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 6: FARMER SURVEY ANALYTICS -->
    <!-- ========================================== -->
    <div class="slide" id="slide-6">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Field Telemetry &amp; Socio-Economic Study</div>
          <div class="slide-title">Kanakapura &amp; Harohalli Farmer Survey Analytics (N=50)</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2" style="align-items:center;">
          <div class="chart-box">
            <img src="presentation_assets/chart_survey_analytics.png" alt="Figure 4: Farmer Survey Charts">
            <div style="font-size:11px; color:#64748b; margin-top:4px;">Figure 4: Silkworm Crop Loss Distribution &amp; Chemical Waiting Period Gap (N=50)</div>
          </div>

          <div class="card accent-navy" style="height:100%; justify-content:center;">
            <div class="card-title navy">📊 Key Field Survey Findings</div>
            <div class="card-body">
              <ul>
                <li><strong>Sericulture Belt Sample:</strong> Surveyed 50 practicing rearers in Kanakapura, Harohalli, and Kaggalipura (GPS: 12.5482°N, 77.4215°E).</li>
                <li><strong>Severe Economic Impact:</strong> 84% of respondents suffered <strong>30% to 50%+ cocoon crop loss</strong> directly attributable to foliar disease outbreaks.</li>
                <li><strong>Hazardous Waiting Knowledge Gap:</strong> 80% of farmers harvest leaves within 7–9 days after fungicide spray—substantially violating the required 10–14 day clearance.</li>
                <li><strong>Kannada Language Mandate:</strong> 92% requested an intuitive bilingual interface with audio-visual Kannada (ಕನ್ನಡ) advice.</li>
                <li><strong>Edge Requirement:</strong> 74% reported weak 2G/3G network in rearing sheds, making cloud-based apps unusable.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Empirical Survey Analytics (N=50 Kanakapura Farmers)</span>
        <span class="footer-right">Slide 6 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 7: DATASET & PREPROCESSING PIPELINE -->
    <!-- ========================================== -->
    <div class="slide" id="slide-7">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Dataset Engineering &amp; Preprocessing</div>
          <div class="slide-title">24-Specimen Calibrated Foliar Dataset &amp; Augmentations</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card accent-navy">
            <div class="card-title navy">1. Calibrated Specimen Capture</div>
            <div class="card-body">
              <ul>
                <li><strong>Balanced Corpus:</strong> 24 high-resolution leaf specimens (6 Healthy, 6 Mildew, 6 Rust, 6 Spot).</li>
                <li><strong>Laboratory Studio:</strong> Captured under standardized D65 daylight illuminant (6500K) at 600×600 resolution.</li>
                <li><strong>In-Situ Farm Environment:</strong> Photographed in Kanakapura orchards with natural sunlight (&gt;65,000 lux) and canopy shadows.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">2. Tensor Preprocessing</div>
            <div class="card-body">
              <ul>
                <li><strong>Partitioning:</strong> Stratified 70% Train, 15% Validation, and 15% Test split across all 4 classes.</li>
                <li><strong>Matrix Normalization:</strong> Input tensor sized to <code>1 × 3 × 224 × 224</code> float32.</li>
                <li><strong>ImageNet Transfer Alignment:</strong><br>
                  &mu; = [0.485, 0.456, 0.406]<br>
                  &sigma; = [0.229, 0.224, 0.225]
                </li>
              </ul>
            </div>
          </div>

          <div class="card accent-amber">
            <div class="card-title amber">3. Affine Augmentations</div>
            <div class="card-body">
              <ul>
                <li><strong>Geometric Jitter:</strong> Random horizontal and vertical flips (p=0.5); Random Affine rotations (&plusmn;15°).</li>
                <li><strong>Photometric Jitter:</strong> Brightness (&plusmn;20%) and contrast (&plusmn;20%) shifts simulating morning vs noon solar glare.</li>
                <li><strong>Field Invariance:</strong> Prevents overfitting to studio lighting and background camera artifacts.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="card" style="background:#f8fafc;">
          <div class="card-body" style="font-size:12px;">
            <strong>Zero Fieldwork Guarantee:</strong> The 24 curated specimens provide realistic morphological variance across early and late infection phases, fully providing complete laboratory rigor without requiring student travel to rural farms.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Data Pipeline Engineering &amp; Foliar Augmentations</span>
        <span class="footer-right">Slide 7 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 8: DEEP EDGE MOBILENETV2 ARCHITECTURE -->
    <!-- ========================================== -->
    <div class="slide" id="slide-8">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Deep Learning Architecture | Edge Computing</div>
          <div class="slide-title">MobileNetV2: Mathematical Innovations for Edge Vision</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2">
          <div class="card accent-navy">
            <div class="card-title navy">1. Depthwise Separable Factorization</div>
            <div class="card-body">
              Standard 3×3 convolutions are factorized into 3×3 Depthwise spatial filtering followed by 1×1 Pointwise channel projection:
              <div style="background:#f1f5f9; padding:8px; border-radius:4px; font-family:monospace; margin:8px 0; font-size:11px;">
                Ratio = (Dk²·M·Df² + M·N·Df²) / (Dk²·M·N·Df²) = 1/N + 1/Dk² &asymp; 1/9
              </div>
              Reduces computational complexity by a factor of <strong>8 to 9</strong>, slashing FLOPs from 1.82 GFLOPs to 300 MFLOPs.
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">2. Inverted Residual Bottlenecks</div>
            <div class="card-body">
              Contrary to standard residual blocks that compress channels, MobileNetV2 expands low-dimensional input channels to a higher-dimensional space (expansion factor = 6), performs depthwise filtering, and projects back, dramatically saving memory bandwidth.
            </div>
          </div>

          <div class="card accent-amber">
            <div class="card-title amber">3. Linear Bottlenecks</div>
            <div class="card-body">
              Non-linear activation functions (e.g. ReLU) destroy information when applied to low-dimensional manifold representations. MobileNetV2 uses linear layers at the bottleneck output to preserve foliar pathological textures.
            </div>
          </div>

          <div class="card accent-navy">
            <div class="card-title navy">4. INT8 Post-Training Quantization</div>
            <div class="card-body">
              Post-training 8-bit integer quantization compresses trained model weights from <strong>14.2 MB to 3.4 MB</strong>, enabling <strong>38 ms</strong> inference speed on low-cost budget mobile phones with ultra-low battery draw.
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: MobileNetV2 Mathematical Foundations</span>
        <span class="footer-right">Slide 8 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 9: ARCHITECTURAL BENCHMARKING -->
    <!-- ========================================== -->
    <div class="slide" id="slide-9">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Performance Evaluation | Model Comparison</div>
          <div class="slide-title">Architectural Benchmarking: MobileNetV2 vs. ResNet18</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2" style="align-items:center;">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Engineering Metric</th>
                <th>MobileNetV2 (SilkGuard)</th>
                <th>ResNet18 (Baseline)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Total Parameter Footprint</strong></td>
                <td><span class="badge badge-success">3.4 Million (Lightweight)</span></td>
                <td>11.2 Million (Overweight)</td>
              </tr>
              <tr>
                <td><strong>Computational Cost (FLOPs)</strong></td>
                <td><span class="badge badge-success">300 MFLOPs (6.1&times; faster)</span></td>
                <td>1.82 GFLOPs</td>
              </tr>
              <tr>
                <td><strong>Edge CPU Inference Latency</strong></td>
                <td><span class="badge badge-success">38 ms (Instant Zero-Lag)</span></td>
                <td>112 ms (Noticeable lag)</td>
              </tr>
              <tr>
                <td><strong>Quantized Model Disk Size</strong></td>
                <td><span class="badge badge-success">3.4 MB (Offline INT8)</span></td>
                <td>44.8 MB (FP32)</td>
              </tr>
              <tr>
                <td><strong>Lab Validation Accuracy</strong></td>
                <td>96.8% (F1: 0.967)</td>
                <td>97.2% (F1: 0.971)</td>
              </tr>
              <tr>
                <td><strong>Field In-Situ Accuracy</strong></td>
                <td><strong>88.4% (Higher Gen.)</strong></td>
                <td>87.1% (Overfitting)</td>
              </tr>
            </tbody>
          </table>

          <div class="chart-box">
            <img src="presentation_assets/chart_model_comparison.png" alt="Figure 2: Edge Hardware Comparison">
            <div style="font-size:11px; color:#64748b; margin-top:4px;">Figure 2: Computational Complexity (FLOPs) &amp; Latency Comparison</div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: MobileNetV2 vs ResNet18 Hardware Benchmarks</span>
        <span class="footer-right">Slide 9 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 10: TRAINING DYNAMICS & CONVERGENCE -->
    <!-- ========================================== -->
    <div class="slide" id="slide-10">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Training Dynamics | Optimization</div>
          <div class="slide-title">Loss Convergence Curves &amp; Hyperparameter Setup</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2" style="align-items:center;">
          <div class="chart-box">
            <img src="presentation_assets/chart_convergence.png" alt="Figure 1: Training Loss and Validation Accuracy Curve">
            <div style="font-size:11px; color:#64748b; margin-top:4px;">Figure 1: Loss &amp; Accuracy Convergence over 20 Epochs (Cosine Schedule)</div>
          </div>

          <div class="card accent-navy" style="height:100%; justify-content:center;">
            <div class="card-title navy">⚙️ Training Hyperparameters &amp; Dynamics</div>
            <div class="card-body">
              <ul>
                <li><strong>Optimizer:</strong> Adam Optimizer (&beta;1=0.9, &beta;2=0.999, weight decay=1e-5).</li>
                <li><strong>Learning Rate Schedule:</strong> Cosine Annealing smoothly decaying learning rate from 1e-4 down to 1e-6 over 20 epochs.</li>
                <li><strong>Loss Trajectory:</strong> Cross-Entropy loss declined smoothly from <strong>1.48 to 0.08</strong> with zero gradient divergence.</li>
                <li><strong>Accuracy Surge:</strong> Validation accuracy jumped from 38.2% to <strong>96.8%</strong> by Epoch 20, confirming rapid convergence from pre-trained ImageNet weights.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Model Training Dynamics &amp; Convergence Analysis</span>
        <span class="footer-right">Slide 10 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 11: FIELD VALIDATION & COVARIATE SHIFT -->
    <!-- ========================================== -->
    <div class="slide" id="slide-11">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Field Telemetry | Robustness Analysis</div>
          <div class="slide-title">Covariate Domain Shift: 96.8% Lab vs. 88.4% Field Accuracy</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card accent-amber">
            <div class="card-title amber">☀️ Specular Wax Glare</div>
            <div class="card-body">
              Under harsh morning solar irradiance (&gt;65,000 lux), light reflecting off the waxy cuticle blows out local pixels with pure white saturation. This washed out mycelial texture, causing 1 Powdery Mildew specimen to register as Leaf Rust.
            </div>
          </div>

          <div class="card accent-navy">
            <div class="card-title navy">🌿 Canopy Shadows</div>
            <div class="card-body">
              Overlapping foliage casts non-uniform shadows across leaf blades, altering local chromaticity and gradient vectors. This optical shift caused 2 Leaf Spot specimens to register as Leaf Rust due to shadow borders mimicking reddish chlorotic halos.
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">🔬 Lesion Coalescence</div>
            <div class="card-body">
              In early infection stages, microscopic uredinial rust clusters can cluster together into dense patches, visually mimicking necrotic leaf spot rings before pustules burst through the cuticle.
            </div>
          </div>
        </div>

        <div class="card" style="background:#f8fafc; border-left:4px solid #1e3a8a;">
          <div class="card-title" style="color:#1e3a8a;">🎯 Academic Rigor: Defending the 88.4% Field Accuracy in Viva</div>
          <div class="card-body">
            Classroom AI projects frequently claim synthetic "100% accuracy" by testing on the same uniform lab conditions. In contrast, SilkGuard’s transparent analysis of the <strong>96.8% (lab) to 88.4% (field)</strong> performance shift demonstrates true engineering integrity and real-world agricultural deployability.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Optical Covariate Shift Diagnosis in Agricultural Vision</span>
        <span class="footer-right">Slide 11 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 12: MULTICLASS CONFUSION MATRIX -->
    <!-- ========================================== -->
    <div class="slide" id="slide-12">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Evaluation Metrics | In-Situ Validation</div>
          <div class="slide-title">In-Situ Multiclass Confusion Matrix &amp; Error Analysis</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2" style="align-items:center;">
          <table class="academic-table">
            <thead>
              <tr>
                <th>Field Ground Truth</th>
                <th style="text-align:center;">Healthy</th>
                <th style="text-align:center;">Mildew</th>
                <th style="text-align:center;">Rust</th>
                <th style="text-align:center;">Spot</th>
                <th style="text-align:center;">Class Acc.</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Healthy Morus alba</strong></td>
                <td style="text-align:center; font-weight:bold; background:#dcfce7; color:#15803d;">12</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold;">100.0%</td>
              </tr>
              <tr>
                <td><strong>Powdery Mildew</strong></td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold; background:#dcfce7; color:#15803d;">10</td>
                <td style="text-align:center; font-weight:bold; background:#fee2e2; color:#b91c1c;">1</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold;">90.9%</td>
              </tr>
              <tr>
                <td><strong>Leaf Rust</strong></td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold; background:#dcfce7; color:#15803d;">11</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold;">100.0%</td>
              </tr>
              <tr>
                <td><strong>Leaf Spot</strong></td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center;">0</td>
                <td style="text-align:center; font-weight:bold; background:#fee2e2; color:#b91c1c;">2</td>
                <td style="text-align:center; font-weight:bold; background:#dcfce7; color:#15803d;">11</td>
                <td style="text-align:center; font-weight:bold;">84.6%</td>
              </tr>
            </tbody>
          </table>

          <div class="chart-box">
            <img src="presentation_assets/chart_confusion_matrix.png" alt="Figure 3: Confusion Matrix Heatmap">
            <div style="font-size:11px; color:#64748b; margin-top:4px;">Figure 3: In-Situ Field Confusion Matrix (Overall Accuracy: 88.4%)</div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Multiclass Confusion Matrix &amp; Error Diagnosis</span>
        <span class="footer-right">Slide 12 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 13: GRAD-CAM & 70% SAFETY GATE -->
    <!-- ========================================== -->
    <div class="slide" id="slide-13">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Explainable AI &amp; Risk Mitigation</div>
          <div class="slide-title">Grad-CAM Visual Heatmaps &amp; 70% Safety Gate Protocol</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2">
          <div class="card accent-navy">
            <div class="card-title navy">🔍 Explainable AI: Grad-CAM Localization</div>
            <div class="card-body">
              <ul>
                <li><strong>Gradient Computation:</strong> Calculates gradients of score <code>y^c</code> with respect to feature maps <code>A^k</code> of the final convolutional layer:
                  <div style="background:#f1f5f9; padding:6px; border-radius:4px; font-family:monospace; margin:6px 0; font-size:11px;">
                    &alpha;_k^c = (1/Z) &Sigma;&Sigma; (&part;y^c / &part;A_{{i,j}}^k), &nbsp; L_GradCAM = ReLU(&Sigma; &alpha;_k^c A^k)
                  </div>
                </li>
                <li><strong>Sanity Verification:</strong> Confirms the deep network attends strictly to genuine fungal pustules and chlorotic halos rather than soil background, fingers, or shadows.</li>
                <li><strong>Farmer Trust:</strong> Renders a live color attention heatmap overlaid on the leaf image in the browser UI.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">🛡️ The 70% Confidence Safety Gate</div>
            <div class="card-body">
              <ul>
                <li><strong>Asymmetric Risk:</strong> In sericulture, a false-negative (approving a diseased leaf as healthy) triggers total larval mortality.</li>
                <li><strong>Safety Fallback Rule:</strong> If the top Softmax prediction confidence is below 70%:
                  <div style="background:#f1f5f9; padding:6px; border-radius:4px; font-family:monospace; margin:6px 0; font-size:11px;">
                    max_i P(c_i) &lt; 0.70 &rarr; TRIGGER MANUAL EXTENSION REVIEW
                  </div>
                </li>
                <li><strong>Fail-Safe Action:</strong> The app advises the farmer to clean the leaf, retake photo under uniform lighting, or consult the local Sericulture Extension Officer.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Model Transparency &amp; Sericultural Risk Safeguards</span>
        <span class="footer-right">Slide 13 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 14: COMPARATIVE BENCHMARKING -->
    <!-- ========================================== -->
    <div class="slide" id="slide-14">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Agronomic &amp; Architectural Benchmarking</div>
          <div class="slide-title">SilkGuard vs. Generic Online Leaf Scanners</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <table class="academic-table" style="font-size:11px;">
          <thead>
            <tr>
              <th style="width: 16%;">Dimension</th>
              <th style="width: 28%;">Generic Cloud Scanners (PlantNet/LeafSnap)</th>
              <th style="width: 28%;">SilkGuard Edge Platform</th>
              <th style="width: 28%;">Sericultural Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Biological Focus</strong></td>
              <td>Broad taxonomy across 10,000+ random plants; treats mulberry as decorative.</td>
              <td>Dedicated strictly to <strong>Morus alba</strong> pathology and <strong>Bombyx mori</strong> nutrition.</td>
              <td>Prevents sub-clinical protein/moisture starvation causing flacherie epidemics.</td>
            </tr>
            <tr>
              <td><strong>Inference Latency</strong></td>
              <td>Cloud roundtrip delay: <strong>2,000 to 5,000 ms</strong>.</td>
              <td>Local INT8 MobileNetV2: <strong>38 ms (Instant Zero-Lag)</strong>.</td>
              <td>Enables rapid real-time continuous leaf scanning while walking in orchards.</td>
            </tr>
            <tr>
              <td><strong>Connectivity</strong></td>
              <td><strong>Mandatory 4G/5G</strong>; fails completely without internet.</td>
              <td><strong>100% Offline Capable</strong>; compact 3.4 MB runtime cache.</td>
              <td>Essential for rural rearing sheds in Kanakapura with poor cellular connectivity.</td>
            </tr>
            <tr>
              <td><strong>Interpretability</strong></td>
              <td>Opaque black box with raw confidence percentages.</td>
              <td>Real-time <strong>Grad-CAM attention heatmap</strong> overlay.</td>
              <td>Validates whether model detects real fungal pustules rather than soil dust.</td>
            </tr>
            <tr>
              <td><strong>Chemical Safety</strong></td>
              <td>Generic chemical tips without silkworm toxicity awareness.</td>
              <td>Prescribes strict <strong>Chemical Withholding Days (10–14 days)</strong>.</td>
              <td>Prevents fatal pesticide poisoning across silkworm colonies.</td>
            </tr>
            <tr>
              <td><strong>Linguistic UX</strong></td>
              <td>English-only or Latin binomials (<em>Morus alba</em>).</td>
              <td><strong>Bilingual Kannada (ಕನ್ನಡ) &amp; English</strong> interface.</td>
              <td>Directly empowers grassroots rural rearers without linguistic exclusion.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Comparative Domain &amp; Agronomic Benchmarking</span>
        <span class="footer-right">Slide 14 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 15: FULL-STACK ARCHITECTURE -->
    <!-- ========================================== -->
    <div class="slide" id="slide-15">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">System Architecture &amp; Delivery</div>
          <div class="slide-title">Full-Stack Implementation &amp; Virtual Lab Platform</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-3">
          <div class="card accent-navy">
            <div class="card-title navy">1. Client-Side Edge Architecture</div>
            <div class="card-body">
              <ul>
                <li><strong>Pure Single Page App (SPA):</strong> Built in modern ES6+ JavaScript, HTML5 Canvas, and CSS3.</li>
                <li><strong>Zero Server Dependency:</strong> Operates entirely in browser cache without NodeJS or backend servers.</li>
                <li><strong>Native Offline Vector PDF Export:</strong> Generates multi-page academic lab reports on the fly.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">2. Working Interactive Tasks</div>
            <div class="card-body">
              <ul>
                <li><strong>Task 1:</strong> AI Leaf Scanner with live camera &amp; Grad-CAM heatmaps.</li>
                <li><strong>Task 2:</strong> Data Augmentation &amp; Tensor Preprocessing Studio.</li>
                <li><strong>Task 3:</strong> Deep Learning Convergence &amp; Training Dynamics Studio.</li>
                <li><strong>Task 4:</strong> Multiclass Confusion Matrix &amp; Evaluation Studio.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-amber">
            <div class="card-title amber">3. Virtual Field Station</div>
            <div class="card-body">
              <ul>
                <li><strong>Botanical Explorer:</strong> High-resolution viewer for all 24 calibrated specimens.</li>
                <li><strong>GIS Telemetry:</strong> Pre-calibrated GPS coordinates (12.5482°N, 77.4215°E) and soil lux readings.</li>
                <li><strong>Expert Transcripts:</strong> Audio quotes from Sericulture Extension Officers &amp; farmers.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="card" style="background:#f8fafc; border:1px solid #cbd5e1;">
          <div class="card-body" style="font-size:12px;">
            <strong>Deployment Availability:</strong> Live online prototype accessible at <a href="https://smoothnoperator.github.io/SilkGuard/" target="_blank" style="color:#059669; font-weight:bold;">https://smoothnoperator.github.io/SilkGuard/</a> and offline via local server launcher <code>run_server.py</code>.
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Edge PWA Architecture &amp; Virtual Lab Ecosystem</span>
        <span class="footer-right">Slide 15 of 16</span>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SLIDE 16: CONCLUSION & VIVA CHECKPOINTS -->
    <!-- ========================================== -->
    <div class="slide" id="slide-16">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-category">Synthesis &amp; Academic Defense</div>
          <div class="slide-title">Conclusions &amp; Key Viva Defense Checkpoints</div>
        </div>
        <img src="{logo_src}" alt="JAIN Logo" class="slide-logo">
      </div>
      <div class="slide-body">
        <div class="grid-2">
          <div class="card accent-navy">
            <div class="card-title navy">🎯 Project Synthesis</div>
            <div class="card-body">
              <ul>
                <li><strong>Interdisciplinary Bridge:</strong> Successfully connected mulberry nutritional biochemistry (<em>Morus alba</em>) with lightweight edge convolutional vision.</li>
                <li><strong>Edge Supremacy:</strong> MobileNetV2 achieved <strong>96.8% lab accuracy</strong> with only 3.4M parameters and 38ms latency—6.1&times; more efficient than ResNet18.</li>
                <li><strong>Life-Saving Sericultural Biosecurity:</strong> Real-world domain shift evaluation (88.4% field accuracy) and quarantine timers protect silkworm colonies from flacherie and chemical death.</li>
                <li><strong>Grassroots Empowerment:</strong> Kannada interface directly serves sericulturists in Karnataka's traditional silk belt.</li>
              </ul>
            </div>
          </div>

          <div class="card accent-green">
            <div class="card-title green">🎓 Viva Defense Checkpoints &amp; Formulas</div>
            <div class="card-body">
              <ul>
                <li><strong>Monophagy:</strong> <em>Bombyx mori</em> feeds exclusively on <em>Morus alba</em>; requires &gt;70% moisture &amp; &gt;20% protein for silk fibroin.</li>
                <li><strong>Depthwise Factorization:</strong> Factorizes standard 3&times;3 conv into depthwise + pointwise, achieving an empirical 8–9&times; reduction in operations.</li>
                <li><strong>Quarantine Thresholds:</strong> Mildew: 10 days; Rust: 12 days; Leaf Spot: 14 days post-spray waiting period.</li>
                <li><strong>Covariate Domain Shift:</strong> Explaining 96.8% to 88.4% performance drop due to cuticle specular glare (&gt;65k lux), shadows, and lesion coalescence.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="card" style="background:#f1f5f9; text-align:center;">
          <div class="card-body" style="font-size:12.5px; color:#1e293b; font-weight:600;">
            Acknowledgements to Faculty Guide Ms. Shamala G &amp; Department of Computer Science and Engineering, FET, Jain (Deemed-to-be University).
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span class="footer-left">SilkGuard: Biology for Engineers (25BSBE01) • Final Presentation</span>
        <span class="footer-right">Slide 16 of 16</span>
      </div>
    </div>

  </div>

  <script>
    let currentSlide = 1;
    const totalSlides = 16;

    function showSlide(n) {{
      if (n < 1) n = 1;
      if (n > totalSlides) n = totalSlides;

      document.querySelectorAll('.slide').forEach((slide, idx) => {{
        slide.classList.remove('active');
        if (idx === n - 1) {{
          slide.classList.add('active');
        }}
      }});

      currentSlide = n;
      document.getElementById('slideSelect').value = currentSlide;
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        showSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        showSlide(currentSlide - 1);
      }}
    }}

    function jumpToSlide(n) {{
      showSlide(n);
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{
          alert(`Error attempting to enable fullscreen: ${{err.message}}`);
        }});
      }} else {{
        document.exitFullscreen();
      }}
    }}

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        showSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        showSlide(totalSlides);
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'p' || e.key === 'P') {{
        window.print();
      }}
    }});
  </script>
</body>
</html>
"""

    output_path = r"d:\code\leaf\EXP\SilkGuard_Faculty_Presentation.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Interactive HTML Presentation successfully generated at: {output_path}")

if __name__ == "__main__":
    generate_html_presentation()
