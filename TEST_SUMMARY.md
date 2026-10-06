# AthleteGuard AI — Test Execution Summary

**Execution Time**: 2026-09-24 04:23:00 UTC  
**Total Duration**: 1545.42 seconds  
**Target Environment**: Windows 10, MySQL `athleteguard_db` (localhost:3306), Python 3.13 Flask 3.1  

## 1. Test Statistics

| Metric | Value |
| :--- | :--- |
| **Total Test Cases Executed** | **66** |
| **Passed** | **36** |
| **Failed** | **30** |
| **Skipped** | **0** |
| **Pass Percentage** | **54.55%** |

---

## 2. Test Case Results Matrix

| Test ID | Module | Test Description | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `test_admin_001_login` | `test_admin` | ADMIN-001: Admin login with valid credentials. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_002_dashboard_loads` | `test_admin` | ADMIN-002: Admin dashboard page rendering. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_003_stats_api` | `test_admin` | ADMIN-003: Admin statistics API returns live database counts. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_004_to_006_athletes_roster_search_filter` | `test_admin` | ADMIN-004 to ADMIN-006: Athlete roster listing, search, and sport filtering. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_007_athlete_detail` | `test_admin` | ADMIN-007: Admin detail view for specific athlete. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_008_health_records` | `test_admin` | ADMIN-008: Admin health records global list. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_009_predictions` | `test_admin` | ADMIN-009: Admin predictions list. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_admin_010_to_012_case_review_notes_notification` | `test_admin` | ADMIN-010 to ADMIN-012: Case review, status update, admin notes, and athlete notification visibility. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_admin_013_deactivate_activate_athlete` | `test_admin` | ADMIN-013: Admin deactivates and reactivates athlete account. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_admin_014_logout` | `test_admin` | ADMIN-014: Admin logout. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_api_404_non_existent_endpoint` | `test_api` | Verify requesting invalid API route returns 404. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_api_latency_and_schema` | `test_api` | Verify API response returns in under 2 seconds and contains expected JSON keys. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_001_valid_registration` | `test_auth` | TC-AUTH-001: Valid athlete registration creates account in MySQL DB. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_002_duplicate_email` | `test_auth` | TC-AUTH-002: Duplicate email registration is rejected. | Success / Valid Response | AssertionError: b'already registered' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="9f730bd29ab88cf42847570eb0d564b81bf2bcabb3f9142073a3da382f00a548">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">automation test athlete 1790222247968</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">automation test athlete 1790222247968</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, automation test athlete 1790222247968 \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html><!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="AthleteGuard AI - Explainable Sports Injury Prediction & Athlete Performance Management System">\n  <meta name="csrf-token" content="9f730bd29ab88cf42847570eb0d564b81bf2bcabb3f9142073a3da382f00a548">\n  <title>Athlete Dashboard - AthleteGuard AI</title>\n\n  <!-- Google Fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- Bootstrap 5 CSS -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- Font Awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- Chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- Custom Master Stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- Sidebar Navigation -->\n  <aside class="app-sidebar" id="appSidebar">\n    <div>\n      <!-- Brand Header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">AthleteGuard AI</div>\n            <span class="ai-badge">AI POWERED</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- Navigation Links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>Dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>Profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>Medical History</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>Daily Health Monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>Prediction History</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>Weekly Summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>Monthly Summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>Join Team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>My Team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- User Profile Widget & Logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          A\n        </div>\n        <div class="user-info">\n          <div class="user-name">Automation Test Athlete 1790222247968</div>\n          <span class="user-sport-badge">Football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="Sign Out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- Main Content Area -->\n  <div class="app-main">\n    \n    <!-- Top Header Bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebarToggle" aria-label="Toggle Navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">Dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- Dynamic ML Model Status Indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headerModelStatus">Random Forest Model Active</span>\n        </div>\n\n        <!-- Athlete Notifications Bell Dropdown -->\n        <div class="dropdown me-2" id="athleteNotificationDropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnNotificationBell" title="Notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationBadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> Notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnMarkAllRead" onclick="markAllNotificationsRead(event)">Mark all as read</button>\n            </div>\n            \n            <div id="notificationsList" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> Loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            A\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">Automation Test Athlete 1790222247968</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> Logout\n        </a>\n      </div>\n    </header>\n\n    <!-- Dashboard Main Content -->\n    <main class="dashboard-content">\n      \n      <!-- Welcome Hero Section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">Welcome back, Automation Test Athlete 1790222247968 \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">Monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentDateDisplay">Thursday, 13 August 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> Start Daily Monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- Loading State Spinner Overlay -->\n      <div id="dashboardLoading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">Loading Dashboard Data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">Retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- Professional Error State Banner -->\n      <div id="dashboardErrorBanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">Unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">Please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retryDashboardFetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> Try Again\n          </button>\n        </div>\n      </div>\n\n      <!-- Professional Empty State -->\n      <div id="dashboardEmptyState" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">No injury predictions yet</h3>\n        <p class="empty-state-text">Complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> Start Health Assessment\n        </a>\n      </div>\n\n      <!-- Main Statistics & Analytics Grid -->\n      <div id="dashboardMainGrid">\n        \n        <!-- 4 Statistics Cards Section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Current Risk</span>\n                <div class="stat-card-val text-success" id="statRiskPercent">18%</div>\n                <div class="stat-card-sub">Low Risk \xe2\x80\xa2 Latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Total Predictions</span>\n                <div class="stat-card-val" id="statTotalPredictions">12</div>\n                <div class="stat-card-sub">Last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Avg Sleep</span>\n                <div class="stat-card-val" id="statAvgSleep">7.4 hrs</div>\n                <div class="stat-card-sub">Based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Avg Training</span>\n                <div class="stat-card-val" id="statAvgTraining">3.2 hrs</div>\n                <div class="stat-card-sub">Average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- Prominent Risk Score Card & Today\'s Health Overview Row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- Current Injury Risk Score Card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> Current Injury Risk Score\n                </h3>\n                <span class="badge bg-success" id="riskLevelBadge">LOW RISK</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskCircleGauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskGaugeNumber">18%</span>\n                    <span class="risk-label">INJURY RISK</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskHeadingText">Low Injury Risk Detected</h4>\n                  <p class="mb-2">Based on the latest health monitoring data and Random Forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>Last Prediction: <strong class="text-dark" id="riskLastPredictionDate">13 August 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- Prediction Summary Component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Risk Level</span>\n                    <span class="prediction-summary-val text-success" id="summaryRiskLevel">Low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Risk Score</span>\n                    <span class="prediction-summary-val" id="summaryRiskScore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Predicted On</span>\n                    <span class="prediction-summary-val" id="summaryPredictedOn">13 Aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      View Prediction Details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- Today\'s Health Overview Card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> Today\'s Health Overview\n                </h3>\n                <span class="badge bg-light text-dark border">Latest Entry</span>\n              </div>\n\n              <div id="todaysOverviewContainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Sleep</span>\n                  <strong class="text-dark fs-6" id="todaySleepVal">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Training Hours</span>\n                  <strong class="text-dark fs-6" id="todayTrainingVal">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Resting Heart Rate</span>\n                  <strong class="text-dark fs-6" id="todayHeartRateVal">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Fatigue</span>\n                  <strong class="text-success fs-6" id="todayFatigueVal">Low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Stress</span>\n                  <strong class="text-warning fs-6" id="todayStressVal">Moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Previous Injury</span>\n                  <strong class="text-dark fs-6" id="todayInjuryVal">No</strong>\n                </div>\n              </div>\n\n              <!-- Fallback View when No Today Data -->\n              <div id="todaysOverviewFallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">No health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> Start Daily Monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- Health Trends Line Chart & Risk Distribution Doughnut Row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- Health Trends Line Chart Card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> Health Trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="Time Filter">\n                  <button type="button" id="filter7Days" class="btn btn-sm btn-primary active">7 Days</button>\n                  <button type="button" id="filter30Days" class="btn btn-sm btn-outline-secondary">30 Days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthTrendsChartCanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- Risk Distribution Doughnut Chart Card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> Prediction Risk Distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 Days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskDistributionChartCanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- Recent Predictions Table Card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> Recent Predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              View All Predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>Date</th>\n                  <th>Risk Level</th>\n                  <th>Risk Score</th>\n                  <th>Status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 Aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> Low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 Aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> Medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 Aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> Low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- Quick Actions Section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> Quick Actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Daily Health Monitoring</div>\n                  <div class="quick-action-sub">Record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Prediction History</div>\n                  <div class="quick-action-sub">View past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Weekly Summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Monthly Summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- Bootstrap 5 JS Bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- Master UI JS -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>' | ❌ FAIL |
| `test_tc_auth_003_invalid_empty_fields` | `test_auth` | TC-AUTH-003: Invalid or empty required fields fail registration. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_004_valid_athlete_login` | `test_auth` | TC-AUTH-004: Valid athlete login succeeds and opens dashboard. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_005_invalid_password` | `test_auth` | TC-AUTH-005: Login with wrong password is rejected. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_006_non_existing_account` | `test_auth` | TC-AUTH-006: Login with non-existing email is rejected. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_007_logout` | `test_auth` | TC-AUTH-007: Logout terminates session. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_008_browser_back_protection` | `test_auth` | TC-AUTH-008: Authenticated dashboard cannot be accessed without session after logout. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_tc_auth_009_inactive_athlete_login` | `test_auth` | TC-AUTH-009: Inactive athlete login is blocked. | Success / Valid Response | AssertionError: b'deactivated' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="216da0d8b6bf62289b017a15181c8cb48334f9240d3acd4533b7b661ea6f11d4">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          t\n        </div>\n        <div class="user-info">\n          <div class="user-name">test inactive athlete</div>\n          <span class="user-sport-badge">boxing</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            t\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">test inactive athlete</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, test inactive athlete \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>' | ❌ FAIL |
| `test_athlete_blocked_from_coach_dashboard` | `test_coach` | Verify athlete role is blocked from accessing /coach/dashboard. | Success / Valid Response | AssertionError: b'access denied' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="b99ee7eeccc269d10cf665ded55372e0fdd1c2e2c9c5d2b0f7e29de9f5909b7c">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">athlete coachtesttarget</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">athlete coachtesttarget</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, athlete coachtesttarget \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>' | ❌ FAIL |
| `test_coach_dashboard_page_rendering` | `test_coach` | Verify coach dashboard loads HTML page for authenticated coach. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_coach_login_redirection` | `test_coach` | Verify coach login redirects to /coach/dashboard. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_dashboard_api_empty_state` | `test_dashboard` | Verify dashboard API handles new user with zero predictions gracefully. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_dashboard_api_populated_state` | `test_dashboard` | Verify dashboard API calculates metrics and chart series when records exist. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_dashboard_page_rendering` | `test_dashboard` | Verify dashboard HTML page loads for logged in athlete. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_mysql_connection_and_tables_exist` | `test_database` | Verify active MySQL connection and existence of all required tables. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_user_foreign_key_cascade_or_integrity` | `test_database` | Verify database integrity and column constraints on users table. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_e2e_complete_athlete_lifecycle` | `test_e2e` | TC-E2E-001: Comprehensive End-to-End Athlete Lifecycle Integration Test
Covers all 23 steps required by Section 9 of the test specification. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_health_monitoring_page_loads` | `test_health_monitoring` | Verify daily-monitoring form page loads. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_invalid_health_values_rejected` | `test_health_monitoring` | Verify out-of-bounds health metrics (sleep > 12h, negative resting HR) are rejected. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_valid_health_record_submission` | `test_health_monitoring` | Verify submitting valid daily health parameters persists to MySQL DB. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_add_and_manage_injury` | `test_medical_history` | Verify adding, updating, and deleting an injury record. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_get_medical_history_empty` | `test_medical_history` | Verify fetching medical history for athlete with 0 records. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_medical_history_user_isolation` | `test_medical_history` | Verify Athlete B cannot modify or delete Athlete A's injury record. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/gkpj) | ❌ FAIL |
| `test_medical_history_user_isolation` | `test_medical_history` | Verify Athlete B cannot modify or delete Athlete A's injury record. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/gkpj) (Background on this error at: https://sqlalche.me/e/20/7s2a) | ❌ FAIL |
| `test_high_workload_prediction_escalation` | `test_prediction` | Verify high fatigue, high training hours, and previous injury result in elevated risk score. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_ml_service_direct_prediction` | `test_prediction` | Verify direct ml_service execution produces score (0-100%) and valid risk label. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_prediction_saved_to_history` | `test_prediction` | Verify submitting health monitoring saves prediction and displays in prediction history API. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_profile_data_retrieval_api` | `test_profile` | Verify GET /api/profile returns athlete's profile payload. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/gkpj) | ❌ FAIL |
| `test_profile_gender_validation` | `test_profile` | Verify invalid gender is rejected in profile update. | Success / Valid Response | AssertionError: 'gender must be either male or female' not found in 'csrf token validation failed. invalid or missing csrf token.' | ❌ FAIL |
| `test_profile_gender_validation` | `test_profile` | Verify invalid gender is rejected in profile update. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_profile_page_loading` | `test_profile` | Verify profile HTML page loads for logged-in athlete. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_profile_update_and_persistence` | `test_profile` | Verify updating profile persists to MySQL database. | Success / Valid Response | AssertionError: 400 != 200 | ❌ FAIL |
| `test_profile_update_and_persistence` | `test_profile` | Verify updating profile persists to MySQL database. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_profile_user_isolation` | `test_profile` | Verify Athlete A cannot view or mutate Athlete B's profile via session API. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_athlete_cannot_access_admin_endpoints` | `test_security` | Verify athlete role cannot access admin pages or admin REST APIs. | Success / Valid Response | AssertionError: b'access denied' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="65c8ff8dd685bc15b4fdc762029546bbd6c64ce834ac2452e2bce3d6b7787410">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">athlete securitytest</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">athlete securitytest</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, athlete securitytest \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>' | ❌ FAIL |
| `test_bfcache_security_headers` | `test_security` | Verify anti-caching HTTP headers are returned to prevent back-button dashboard leaks after logout. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_registration_role_tampering_prevention` | `test_security` | Verify submitting role='admin' during registration is ignored and forces role='athlete'. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_unauthenticated_access_blocked` | `test_security` | Verify unauthenticated user cannot access protected endpoints. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_monthly_summary_empty` | `test_summaries` | Verify 30-day monthly summary handles 0 records gracefully. | Success / Valid Response | KeyError: 'total_records' | ❌ FAIL |
| `test_summary_user_isolation` | `test_summaries` | Verify Athlete A's summary does NOT include Athlete B's health records. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_summary_user_isolation` | `test_summaries` | Verify Athlete A's summary does NOT include Athlete B's health records. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) (Background on this error at: https://sqlalche.me/e/20/7s2a) | ❌ FAIL |
| `test_weekly_summary_empty` | `test_summaries` | Verify 7-day weekly summary handles 0 records gracefully. | Success / Valid Response | KeyError: 'total_records' | ❌ FAIL |
| `test_weekly_summary_with_records` | `test_summaries` | Verify 7-day summary calculates exact averages from active records. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_weekly_summary_with_records` | `test_summaries` | Verify 7-day summary calculates exact averages from active records. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) (Background on this error at: https://sqlalche.me/e/20/7s2a) | ❌ FAIL |
| `test_01_coach_login_dashboard` | `test_team` | TEST 1: Coach logs in and reaches Coach Dashboard. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_02_and_03_coach_create_team_and_unique_code` | `test_team` | TEST 2 & 3: Coach creates Football team; unique team code generated and saved to DB. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_04_coach_teams_isolation` | `test_team` | TEST 4: Coach opens My Teams; only that Coach's teams are returned. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_05_athlete_joins_team_valid_code` | `test_team` | TEST 5: Athlete enters valid team code and joins team. | Success / Valid Response | AssertionError: 500 != 200 | ❌ FAIL |
| `test_06_duplicate_membership_prevented` | `test_team` | TEST 6: Athlete attempts to join same team code twice -> rejected. | Success / Valid Response | AssertionError: 500 != 400 | ❌ FAIL |
| `test_07_athlete_views_my_team` | `test_team` | TEST 7: Athlete opens My Team endpoint and views correct membership data. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_08_coach_views_team_members` | `test_team` | TEST 8: Coach opens team details and views active members. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_09_coach_removes_athlete_preserves_data` | `test_team` | TEST 9: Coach removes athlete; membership deactivated; user account, health & medical records preserved. | Success / Valid Response | (Background on this error at: https://sqlalche.me/e/20/e3q8) | ❌ FAIL |
| `test_10_coach_a_cannot_access_coach_b_team` | `test_team` | TEST 10: Coach A attempts to view Coach B's team -> Denied (HTTP 403). | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_11_athlete_cannot_access_coach_team_routes` | `test_team` | TEST 11: Athlete attempts to access coach team-management route -> Redirected/Denied (302). | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_12_unauthenticated_user_team_access` | `test_team` | TEST 12: Unauthenticated user attempts team access -> Login required redirect (302). | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_13_athlete_cannot_create_team` | `test_team` | TEST 13: Athlete attempts to create a team -> Denied (302 redirect or 403). | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_14_coach_cannot_join_team_via_athlete_endpoint` | `test_team` | TEST 14: Coach attempts to join team using athlete endpoint -> Denied (403). | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |
| `test_15_inactive_team_code_rejected` | `test_team` | TEST 15: Athlete tries to join an inactive team code -> Joining rejected. | Success / Valid Response | 200 OK / Database Persisted | ✅ PASS |

---

## 3. Discovered Bugs / Issues Summary

### BUG-001: `test_admin.TestAdmin.test_admin_010_to_012_case_review_notes_notification`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_admin.py", line 138, in test_admin_010_to_012_case_review_notes_notification
    self.assertEqual(res_st.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-002: `test_admin.TestAdmin.test_admin_013_deactivate_activate_athlete`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_admin.py", line 160, in test_admin_013_deactivate_activate_athlete
    self.assertEqual(res_deact.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-003: `test_auth.TestAuth.test_tc_auth_002_duplicate_email`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_auth.py", line 55, in test_tc_auth_002_duplicate_email
    self.assertIn(b"already registered", res.data.lower() + res.data)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: b'already registered' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="9f730bd29ab88cf42847570eb0d564b81bf2bcabb3f9142073a3da382f00a548">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">automation test athlete 1790222247968</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">automation test athlete 1790222247968</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, automation test athlete 1790222247968 \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html><!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="AthleteGuard AI - Explainable Sports Injury Prediction & Athlete Performance Management System">\n  <meta name="csrf-token" content="9f730bd29ab88cf42847570eb0d564b81bf2bcabb3f9142073a3da382f00a548">\n  <title>Athlete Dashboard - AthleteGuard AI</title>\n\n  <!-- Google Fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- Bootstrap 5 CSS -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- Font Awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- Chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- Custom Master Stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- Sidebar Navigation -->\n  <aside class="app-sidebar" id="appSidebar">\n    <div>\n      <!-- Brand Header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">AthleteGuard AI</div>\n            <span class="ai-badge">AI POWERED</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- Navigation Links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>Dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>Profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>Medical History</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>Daily Health Monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>Prediction History</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>Weekly Summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>Monthly Summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>Join Team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>My Team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- User Profile Widget & Logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          A\n        </div>\n        <div class="user-info">\n          <div class="user-name">Automation Test Athlete 1790222247968</div>\n          <span class="user-sport-badge">Football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="Sign Out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- Main Content Area -->\n  <div class="app-main">\n    \n    <!-- Top Header Bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebarToggle" aria-label="Toggle Navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">Dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- Dynamic ML Model Status Indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headerModelStatus">Random Forest Model Active</span>\n        </div>\n\n        <!-- Athlete Notifications Bell Dropdown -->\n        <div class="dropdown me-2" id="athleteNotificationDropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnNotificationBell" title="Notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationBadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> Notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnMarkAllRead" onclick="markAllNotificationsRead(event)">Mark all as read</button>\n            </div>\n            \n            <div id="notificationsList" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> Loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            A\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">Automation Test Athlete 1790222247968</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> Logout\n        </a>\n      </div>\n    </header>\n\n    <!-- Dashboard Main Content -->\n    <main class="dashboard-content">\n      \n      <!-- Welcome Hero Section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">Welcome back, Automation Test Athlete 1790222247968 \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">Monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentDateDisplay">Thursday, 13 August 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> Start Daily Monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- Loading State Spinner Overlay -->\n      <div id="dashboardLoading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">Loading Dashboard Data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">Retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- Professional Error State Banner -->\n      <div id="dashboardErrorBanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">Unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">Please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retryDashboardFetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> Try Again\n          </button>\n        </div>\n      </div>\n\n      <!-- Professional Empty State -->\n      <div id="dashboardEmptyState" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">No injury predictions yet</h3>\n        <p class="empty-state-text">Complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> Start Health Assessment\n        </a>\n      </div>\n\n      <!-- Main Statistics & Analytics Grid -->\n      <div id="dashboardMainGrid">\n        \n        <!-- 4 Statistics Cards Section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Current Risk</span>\n                <div class="stat-card-val text-success" id="statRiskPercent">18%</div>\n                <div class="stat-card-sub">Low Risk \xe2\x80\xa2 Latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Total Predictions</span>\n                <div class="stat-card-val" id="statTotalPredictions">12</div>\n                <div class="stat-card-sub">Last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Avg Sleep</span>\n                <div class="stat-card-val" id="statAvgSleep">7.4 hrs</div>\n                <div class="stat-card-sub">Based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">Avg Training</span>\n                <div class="stat-card-val" id="statAvgTraining">3.2 hrs</div>\n                <div class="stat-card-sub">Average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- Prominent Risk Score Card & Today\'s Health Overview Row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- Current Injury Risk Score Card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> Current Injury Risk Score\n                </h3>\n                <span class="badge bg-success" id="riskLevelBadge">LOW RISK</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskCircleGauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskGaugeNumber">18%</span>\n                    <span class="risk-label">INJURY RISK</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskHeadingText">Low Injury Risk Detected</h4>\n                  <p class="mb-2">Based on the latest health monitoring data and Random Forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>Last Prediction: <strong class="text-dark" id="riskLastPredictionDate">13 August 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- Prediction Summary Component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Risk Level</span>\n                    <span class="prediction-summary-val text-success" id="summaryRiskLevel">Low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Risk Score</span>\n                    <span class="prediction-summary-val" id="summaryRiskScore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">Predicted On</span>\n                    <span class="prediction-summary-val" id="summaryPredictedOn">13 Aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      View Prediction Details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- Today\'s Health Overview Card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> Today\'s Health Overview\n                </h3>\n                <span class="badge bg-light text-dark border">Latest Entry</span>\n              </div>\n\n              <div id="todaysOverviewContainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Sleep</span>\n                  <strong class="text-dark fs-6" id="todaySleepVal">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Training Hours</span>\n                  <strong class="text-dark fs-6" id="todayTrainingVal">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Resting Heart Rate</span>\n                  <strong class="text-dark fs-6" id="todayHeartRateVal">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Fatigue</span>\n                  <strong class="text-success fs-6" id="todayFatigueVal">Low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Stress</span>\n                  <strong class="text-warning fs-6" id="todayStressVal">Moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">Previous Injury</span>\n                  <strong class="text-dark fs-6" id="todayInjuryVal">No</strong>\n                </div>\n              </div>\n\n              <!-- Fallback View when No Today Data -->\n              <div id="todaysOverviewFallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">No health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> Start Daily Monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- Health Trends Line Chart & Risk Distribution Doughnut Row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- Health Trends Line Chart Card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> Health Trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="Time Filter">\n                  <button type="button" id="filter7Days" class="btn btn-sm btn-primary active">7 Days</button>\n                  <button type="button" id="filter30Days" class="btn btn-sm btn-outline-secondary">30 Days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthTrendsChartCanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- Risk Distribution Doughnut Chart Card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> Prediction Risk Distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 Days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskDistributionChartCanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- Recent Predictions Table Card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> Recent Predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              View All Predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>Date</th>\n                  <th>Risk Level</th>\n                  <th>Risk Score</th>\n                  <th>Status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 Aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> Low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 Aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> Medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 Aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> Low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">Completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- Quick Actions Section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> Quick Actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Daily Health Monitoring</div>\n                  <div class="quick-action-sub">Record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Prediction History</div>\n                  <div class="quick-action-sub">View past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Weekly Summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">Monthly Summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- Bootstrap 5 JS Bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- Master UI JS -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>'

```

### BUG-004: `test_auth.TestAuth.test_tc_auth_009_inactive_athlete_login`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_auth.py", line 172, in test_tc_auth_009_inactive_athlete_login
    self.assertIn(b"deactivated", res.data.lower())
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: b'deactivated' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="216da0d8b6bf62289b017a15181c8cb48334f9240d3acd4533b7b661ea6f11d4">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          t\n        </div>\n        <div class="user-info">\n          <div class="user-name">test inactive athlete</div>\n          <span class="user-sport-badge">boxing</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            t\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">test inactive athlete</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, test inactive athlete \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>'

```

### BUG-005: `test_coach.TestCoach.test_athlete_blocked_from_coach_dashboard`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_coach.py", line 62, in test_athlete_blocked_from_coach_dashboard
    self.assertIn(b"access denied", res.data.lower())
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: b'access denied' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="b99ee7eeccc269d10cf665ded55372e0fdd1c2e2c9c5d2b0f7e29de9f5909b7c">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">athlete coachtesttarget</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">athlete coachtesttarget</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, athlete coachtesttarget \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>'

```

### BUG-006: `test_e2e.TestEndToEndWorkflow.test_e2e_complete_athlete_lifecycle`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_e2e.py", line 65, in test_e2e_complete_athlete_lifecycle
    self.assertEqual(res_med.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-007: `test_health_monitoring.TestHealthMonitoring.test_valid_health_record_submission`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_health_monitoring.py", line 55, in test_valid_health_record_submission
    self.assertEqual(res.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-008: `test_medical_history.TestMedicalHistory.test_add_and_manage_injury`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_medical_history.py", line 72, in test_add_and_manage_injury
    self.assertEqual(res.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-009: `test_medical_history.TestMedicalHistory.test_medical_history_user_isolation`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.IntegrityError: (1048, "Column 'recovery_status' cannot be null")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_medical_history.py", line 105, in test_medical_history_user_isolation
    db.session.commit()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1048, "Column 'recovery_status' cannot be null")
[SQL: INSERT INTO injuries (user_id, injury_type, body_part, injury_date, severity, treatment, recovery_status, notes, created_at) VALUES (%(user_id)s, %(injury_type)s, %(body_part)s, %(injury_date)s, %(severity)s, %(treatment)s, %(recovery_status)s, %(notes)s, %(created_at)s)]
[parameters: {'user_id': 402, 'injury_type': 'Ankle Sprain', 'body_part': 'Ankle', 'injury_date': '2026-07-01', 'severity': 'Mild', 'treatment': None, 'recovery_status': None, 'notes': None, 'created_at': datetime.datetime(2026, 9, 24, 3, 57, 43, 71766)}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)

```

### BUG-010: `test_medical_history.TestMedicalHistory.test_medical_history_user_isolation`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_medical_history.py", line 41, in tearDown
    Injury.query.filter_by(user_id=self.athlete.id).delete()
                                   ^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 569, in __get__
    return self.impl.get(state, dict_)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1096, in get
    value = self._fire_loader_callables(state, key, passive)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1126, in _fire_loader_callables
    return state._load_expired(state, passive)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state.py", line 828, in _load_expired
    self.manager.expired_attribute_loader(self, toload, passive)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 1674, in load_scalar_attributes
    result = load_on_ident(
        session,
    ...<4 lines>...
        no_autoflush=no_autoflush,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 510, in load_on_ident
    return load_on_pk_identity(
        session,
    ...<11 lines>...
        is_user_refresh=is_user_refresh,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 695, in load_on_pk_identity
    session.execute(
    ~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<2 lines>...
        bind_arguments=bind_arguments,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2261, in _execute_internal
    conn = self._connection_for_bind(bind)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2113, in _connection_for_bind
    return trans._connection_for_bind(engine, execution_options)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in _connection_for_bind
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 101, in _go
    self._raise_for_prerequisite_state(fn.__name__, current_state)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 975, in _raise_for_prerequisite_state
    raise sa_exc.PendingRollbackError(
    ...<6 lines>...
    )
sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.IntegrityError) (1048, "Column 'recovery_status' cannot be null")
[SQL: INSERT INTO injuries (user_id, injury_type, body_part, injury_date, severity, treatment, recovery_status, notes, created_at) VALUES (%(user_id)s, %(injury_type)s, %(body_part)s, %(injury_date)s, %(severity)s, %(treatment)s, %(recovery_status)s, %(notes)s, %(created_at)s)]
[parameters: {'user_id': 402, 'injury_type': 'Ankle Sprain', 'body_part': 'Ankle', 'injury_date': '2026-07-01', 'severity': 'Mild', 'treatment': None, 'recovery_status': None, 'notes': None, 'created_at': datetime.datetime(2026, 9, 24, 3, 57, 43, 71766)}]
(Background on this error at: https://sqlalche.me/e/20/gkpj) (Background on this error at: https://sqlalche.me/e/20/7s2a)

```

### BUG-011: `test_prediction.TestPrediction.test_prediction_saved_to_history`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_prediction.py", line 77, in test_prediction_saved_to_history
    self.assertEqual(res_pred.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-012: `test_profile.TestProfile.test_profile_data_retrieval_api`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.IntegrityError: (1451, 'Cannot delete or update a parent row: a foreign key constraint fails (`athleteguard_db`.`teams`, CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`coach_id`) REFERENCES `users` (`id`))')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 41, in tearDown
    User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\query.py", line 3217, in delete
    self.session.execute(
    ~~~~~~~~~~~~~~~~~~~~^
        delete_,
        ^^^^^^^^
    ...<3 lines>...
        ),
        ^^
    ),
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2271, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\bulk_persistence.py", line 2033, in orm_execute_statement
    return super().orm_execute_statement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        session, statement, params, execution_options, bind_arguments, conn
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1451, 'Cannot delete or update a parent row: a foreign key constraint fails (`athleteguard_db`.`teams`, CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`coach_id`) REFERENCES `users` (`id`))')
[SQL: DELETE FROM users WHERE users.email LIKE %(email_1)s]
[parameters: {'email_1': '%example.com'}]
(Background on this error at: https://sqlalche.me/e/20/gkpj)

```

### BUG-013: `test_profile.TestProfile.test_profile_gender_validation`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 99, in test_profile_gender_validation
    self.assertIn('gender must be either male or female', data['message'].lower())
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'gender must be either male or female' not found in 'csrf token validation failed. invalid or missing csrf token.'

```

### BUG-014: `test_profile.TestProfile.test_profile_gender_validation`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 41, in tearDown
    User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\query.py", line 3217, in delete
    self.session.execute(
    ~~~~~~~~~~~~~~~~~~~~^
        delete_,
        ^^^^^^^^
    ...<3 lines>...
        ),
        ^^
    ),
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2271, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\bulk_persistence.py", line 2033, in orm_execute_statement
    return super().orm_execute_statement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        session, statement, params, execution_options, bind_arguments, conn
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: DELETE FROM users WHERE users.email LIKE %(email_1)s]
[parameters: {'email_1': '%example.com'}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-015: `test_profile.TestProfile.test_profile_page_loading`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 41, in tearDown
    User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\query.py", line 3217, in delete
    self.session.execute(
    ~~~~~~~~~~~~~~~~~~~~^
        delete_,
        ^^^^^^^^
    ...<3 lines>...
        ),
        ^^
    ),
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2271, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\bulk_persistence.py", line 2033, in orm_execute_statement
    return super().orm_execute_statement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        session, statement, params, execution_options, bind_arguments, conn
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: DELETE FROM users WHERE users.email LIKE %(email_1)s]
[parameters: {'email_1': '%example.com'}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-016: `test_profile.TestProfile.test_profile_update_and_persistence`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 78, in test_profile_update_and_persistence
    self.assertEqual(res.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 400 != 200

```

### BUG-017: `test_profile.TestProfile.test_profile_update_and_persistence`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 41, in tearDown
    User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\query.py", line 3217, in delete
    self.session.execute(
    ~~~~~~~~~~~~~~~~~~~~^
        delete_,
        ^^^^^^^^
    ...<3 lines>...
        ),
        ^^
    ),
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2271, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\bulk_persistence.py", line 2033, in orm_execute_statement
    return super().orm_execute_statement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        session, statement, params, execution_options, bind_arguments, conn
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: DELETE FROM users WHERE users.email LIKE %(email_1)s]
[parameters: {'email_1': '%example.com'}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-018: `test_profile.TestProfile.test_profile_user_isolation`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_profile.py", line 41, in tearDown
    User.query.filter(User.email.like("%example.com")).delete(synchronize_session=False)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\query.py", line 3217, in delete
    self.session.execute(
    ~~~~~~~~~~~~~~~~~~~~^
        delete_,
        ^^^^^^^^
    ...<3 lines>...
        ),
        ^^
    ),
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2271, in _execute_internal
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\bulk_persistence.py", line 2033, in orm_execute_statement
    return super().orm_execute_statement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        session, statement, params, execution_options, bind_arguments, conn
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: DELETE FROM users WHERE users.email LIKE %(email_1)s]
[parameters: {'email_1': '%example.com'}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-019: `test_security.TestSecurity.test_athlete_cannot_access_admin_endpoints`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_security.py", line 57, in test_athlete_cannot_access_admin_endpoints
    self.assertIn(b"access denied", res_page.data.lower())
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: b'access denied' not found in b'<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="description" content="athleteguard ai - explainable sports injury prediction & athlete performance management system">\n  <meta name="csrf-token" content="65c8ff8dd685bc15b4fdc762029546bbd6c64ce834ac2452e2bce3d6b7787410">\n  <title>athlete dashboard - athleteguard ai</title>\n\n  <!-- google fonts -->\n  <link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=inter:wght@300;400;500;600;700;800&family=outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n\n  <!-- bootstrap 5 css -->\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n\n  <!-- font awesome 6 -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n\n  <!-- chart.js 4.x -->\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n\n  <!-- custom master stylesheet -->\n  <link rel="stylesheet" href="/static/css/style.css">\n\n  \n</head>\n<body>\n\n  \n<div class="dashboard-wrapper">\n  \n  <!-- sidebar navigation -->\n  <aside class="app-sidebar" id="appsidebar">\n    <div>\n      <!-- brand header -->\n      <div class="sidebar-header">\n        <a href="/dashboard" class="sidebar-brand">\n          <div class="brand-icon-sm">\n            <i class="fa-solid fa-shield-halved"></i>\n          </div>\n          <div>\n            <div class="brand-title">athleteguard ai</div>\n            <span class="ai-badge">ai powered</span>\n          </div>\n        </a>\n      </div>\n\n      <!-- navigation links -->\n      <nav class="sidebar-nav">\n        <a href="/dashboard" class="nav-item-link active">\n          <i class="fa-solid fa-chart-line"></i>\n          <span>dashboard</span>\n        </a>\n        <a href="/profile" class="nav-item-link">\n          <i class="fa-regular fa-user"></i>\n          <span>profile</span>\n        </a>\n        <a href="/medical-history" class="nav-item-link">\n          <i class="fa-solid fa-notes-medical"></i>\n          <span>medical history</span>\n        </a>\n        <a href="/daily-monitoring" class="nav-item-link">\n          <i class="fa-solid fa-calendar-check"></i>\n          <span>daily health monitoring</span>\n        </a>\n        <a href="/prediction-history" class="nav-item-link">\n          <i class="fa-solid fa-clock-rotate-left"></i>\n          <span>prediction history</span>\n        </a>\n        <a href="/weekly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-week"></i>\n          <span>weekly summary</span>\n        </a>\n        <a href="/monthly-summary" class="nav-item-link">\n          <i class="fa-solid fa-calendar-days"></i>\n          <span>monthly summary</span>\n        </a>\n        <a href="/join-team" class="nav-item-link">\n          <i class="fa-solid fa-right-to-bracket"></i>\n          <span>join team</span>\n        </a>\n        <a href="/my-team" class="nav-item-link">\n          <i class="fa-solid fa-people-group"></i>\n          <span>my team</span>\n        </a>\n      </nav>\n    </div>\n\n    <!-- user profile widget & logout -->\n    <div class="sidebar-footer">\n      <div class="user-profile-widget">\n        <div class="avatar-circle">\n          a\n        </div>\n        <div class="user-info">\n          <div class="user-name">athlete securitytest</div>\n          <span class="user-sport-badge">football</span>\n        </div>\n        <a href="/logout" class="logout-btn-link" title="sign out">\n          <i class="fa-solid fa-right-from-bracket"></i>\n        </a>\n      </div>\n    </div>\n  </aside>\n\n  <!-- main content area -->\n  <div class="app-main">\n    \n    <!-- top header bar -->\n    <header class="app-header">\n      <div class="header-left">\n        <button class="mobile-nav-toggle" id="sidebartoggle" aria-label="toggle navigation">\n          <i class="fa-solid fa-bars"></i>\n        </button>\n        <h1 class="header-title">dashboard</h1>\n      </div>\n\n      <div class="header-right">\n        <!-- dynamic ml model status indicator -->\n        <div class="status-pill-active">\n          <span class="pulse-dot"></span>\n          <span id="headermodelstatus">random forest model active</span>\n        </div>\n\n        <!-- athlete notifications bell dropdown -->\n        <div class="dropdown me-2" id="athletenotificationdropdown">\n          <button class="header-action-icon position-relative border-0 bg-transparent" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="btnnotificationbell" title="notifications">\n            <i class="fa-regular fa-bell fs-5 text-dark"></i>\n            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger" id="notificationbadge" style="display: none; font-size: 0.65rem;">0</span>\n          </button>\n\n          <div class="dropdown-menu dropdown-menu-end shadow-lg border-0 rounded-3 p-0" style="width: 340px; max-height: 420px; overflow-y: auto; z-index: 1060;">\n            <div class="dropdown-header bg-dark text-white rounded-top-3 px-3 py-2.5 d-flex justify-content-between align-items-center">\n              <span class="fw-bold"><i class="fa-solid fa-bell text-info me-1"></i> notifications</span>\n              <button type="button" class="btn btn-link btn-sm text-info text-decoration-none p-0 fs-8 fw-semibold" id="btnmarkallread" onclick="markallnotificationsread(event)">mark all as read</button>\n            </div>\n            \n            <div id="notificationslist" class="p-2">\n              <div class="text-center py-3 text-muted fs-7">\n                <div class="spinner-border spinner-border-sm text-primary me-1"></div> loading notifications...\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <div class="d-flex align-items-center gap-2 ms-2">\n          <div class="avatar-circle" style="width: 36px; height: 36px; font-size: 0.9rem;">\n            a\n          </div>\n          <span class="d-none d-md-inline text-dark fw-semibold fs-7">athlete securitytest</span>\n        </div>\n\n        <a href="/logout" class="btn btn-outline-danger btn-sm rounded-pill px-3 fw-semibold ms-2">\n          <i class="fa-solid fa-sign-out-alt me-1"></i> logout\n        </a>\n      </div>\n    </header>\n\n    <!-- dashboard main content -->\n    <main class="dashboard-content">\n      \n      <!-- welcome hero section -->\n      <div class="athlete-hero-banner mb-4">\n        <div class="d-flex justify-content-between align-items-start flex-wrap gap-3">\n          <div>\n            <h2 class="banner-greeting">welcome back, athlete securitytest \xf0\x9f\x91\x8b</h2>\n            <p class="banner-subtitle mb-2">monitor your health and stay ahead of injury risk.</p>\n            <div class="d-flex align-items-center gap-2 text-white-50 fs-7">\n              <i class="fa-regular fa-calendar text-info"></i>\n              <span id="currentdatedisplay">thursday, 13 august 2026</span>\n            </div>\n          </div>\n          <div>\n            <a href="/daily-monitoring" class="btn btn-light text-primary fw-bold px-4 py-2 rounded-3 shadow-sm">\n              <i class="fa-solid fa-plus-circle me-2"></i> start daily monitoring\n            </a>\n          </div>\n        </div>\n      </div>\n\n      <!-- loading state spinner overlay -->\n      <div id="dashboardloading" class="text-center py-5" style="display: none;">\n        <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">\n          <span class="visually-hidden">loading dashboard data...</span>\n        </div>\n        <p class="text-muted mt-3 fw-medium fs-6">retrieving latest injury risk analytics...</p>\n      </div>\n\n      <!-- professional error state banner -->\n      <div id="dashboarderrorbanner" class="alert alert-danger shadow-sm border-0 rounded-3 mb-4" style="display: none;" role="alert">\n        <div class="d-flex align-items-center justify-content-between">\n          <div class="d-flex align-items-center gap-3">\n            <i class="fa-solid fa-triangle-exclamation fs-3"></i>\n            <div>\n              <h5 class="fw-bold mb-1">unable to load dashboard data</h5>\n              <p class="mb-0 fs-7 opacity-75">please try again.</p>\n            </div>\n          </div>\n          <button class="btn btn-danger btn-sm px-3 fw-semibold rounded-pill" onclick="retrydashboardfetch()">\n            <i class="fa-solid fa-rotate-right me-1"></i> try again\n          </button>\n        </div>\n      </div>\n\n      <!-- professional empty state -->\n      <div id="dashboardemptystate" class="empty-state-container mb-4" style="display: none;">\n        <div class="empty-state-icon">\n          <i class="fa-solid fa-notes-medical"></i>\n        </div>\n        <h3 class="empty-state-title">no injury predictions yet</h3>\n        <p class="empty-state-text">complete your first daily health assessment to receive an injury-risk prediction.</p>\n        <a href="/daily-monitoring" class="btn btn-primary px-4 py-2 fw-semibold rounded-pill shadow-sm">\n          <i class="fa-solid fa-notes-medical me-2"></i> start health assessment\n        </a>\n      </div>\n\n      <!-- main statistics & analytics grid -->\n      <div id="dashboardmaingrid">\n        \n        <!-- 4 statistics cards section -->\n        <div class="row g-3 mb-4">\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-green">\n                <i class="fa-solid fa-heart-pulse"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">current risk</span>\n                <div class="stat-card-val text-success" id="statriskpercent">18%</div>\n                <div class="stat-card-sub">low risk \xe2\x80\xa2 latest prediction</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-blue">\n                <i class="fa-solid fa-chart-pie"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">total predictions</span>\n                <div class="stat-card-val" id="stattotalpredictions">12</div>\n                <div class="stat-card-sub">last 30 days</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-purple">\n                <i class="fa-solid fa-bed"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg sleep</span>\n                <div class="stat-card-val" id="statavgsleep">7.4 hrs</div>\n                <div class="stat-card-sub">based on recent entries</div>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-6 col-lg-3">\n            <div class="stat-card-widget">\n              <div class="stat-icon-wrapper stat-icon-amber">\n                <i class="fa-solid fa-stopwatch"></i>\n              </div>\n              <div>\n                <span class="stat-card-lbl">avg training</span>\n                <div class="stat-card-val" id="statavgtraining">3.2 hrs</div>\n                <div class="stat-card-sub">average daily workload</div>\n              </div>\n            </div>\n          </div>\n        </div>\n\n        <!-- prominent risk score card & today\'s health overview row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- current injury risk score card -->\n          <div class="col-lg-7">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-shield-halved"></i> current injury risk score\n                </h3>\n                <span class="badge bg-success" id="risklevelbadge">low risk</span>\n              </div>\n\n              <div class="risk-meter-container">\n                <div class="risk-circle-gauge" id="riskcirclegauge">\n                  <div class="risk-circle-inner">\n                    <span class="risk-number" id="riskgaugenumber">18%</span>\n                    <span class="risk-label">injury risk</span>\n                  </div>\n                </div>\n\n                <div class="risk-text-details">\n                  <h4 id="riskheadingtext">low injury risk detected</h4>\n                  <p class="mb-2">based on the latest health monitoring data and random forest prediction.</p>\n                  <div class="d-flex align-items-center gap-2 text-muted fs-7">\n                    <i class="fa-regular fa-clock"></i>\n                    <span>last prediction: <strong class="text-dark" id="risklastpredictiondate">13 august 2026</strong></span>\n                  </div>\n                </div>\n              </div>\n\n              <!-- prediction summary component -->\n              <div class="prediction-summary-box">\n                <div class="prediction-summary-grid">\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk level</span>\n                    <span class="prediction-summary-val text-success" id="summaryrisklevel">low</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">risk score</span>\n                    <span class="prediction-summary-val" id="summaryriskscore">18%</span>\n                  </div>\n\n                  <div class="prediction-summary-item">\n                    <span class="prediction-summary-lbl">predicted on</span>\n                    <span class="prediction-summary-val" id="summarypredictedon">13 aug 2026</span>\n                  </div>\n\n                  <div>\n                    <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none p-0 fw-semibold">\n                      view prediction details \xe2\x86\x92\n                    </a>\n                  </div>\n                </div>\n              </div>\n\n            </div>\n          </div>\n\n          <!-- today\'s health overview card -->\n          <div class="col-lg-5">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-heart-circle-check"></i> today\'s health overview\n                </h3>\n                <span class="badge bg-light text-dark border">latest entry</span>\n              </div>\n\n              <div id="todaysoverviewcontainer" class="row g-2 fs-7">\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">sleep</span>\n                  <strong class="text-dark fs-6" id="todaysleepval">7.4 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">training hours</span>\n                  <strong class="text-dark fs-6" id="todaytrainingval">3.2 hrs</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">resting heart rate</span>\n                  <strong class="text-dark fs-6" id="todayheartrateval">72 bpm</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">fatigue</span>\n                  <strong class="text-success fs-6" id="todayfatigueval">low</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">stress</span>\n                  <strong class="text-warning fs-6" id="todaystressval">moderate</strong>\n                </div>\n                <div class="col-6 p-2 bg-light rounded-2 border text-center">\n                  <span class="text-muted d-block fs-8 text-uppercase">previous injury</span>\n                  <strong class="text-dark fs-6" id="todayinjuryval">no</strong>\n                </div>\n              </div>\n\n              <!-- fallback view when no today data -->\n              <div id="todaysoverviewfallback" class="text-center py-4" style="display: none;">\n                <p class="text-muted fs-7 mb-3">no health data recorded today.</p>\n                <a href="/daily-monitoring" class="btn btn-primary btn-sm rounded-pill px-3 fw-semibold">\n                  <i class="fa-solid fa-plus me-1"></i> start daily monitoring\n                </a>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- health trends line chart & risk distribution doughnut row -->\n        <div class="row g-4 mb-4">\n          \n          <!-- health trends line chart card -->\n          <div class="col-lg-8">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-line"></i> health trends\n                </h3>\n                <div class="btn-group" role="group" aria-label="time filter">\n                  <button type="button" id="filter7days" class="btn btn-sm btn-primary active">7 days</button>\n                  <button type="button" id="filter30days" class="btn btn-sm btn-outline-secondary">30 days</button>\n                </div>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="healthtrendschartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n          <!-- risk distribution doughnut chart card -->\n          <div class="col-lg-4">\n            <div class="card-master">\n              <div class="card-header-master">\n                <h3 class="card-title-master">\n                  <i class="fa-solid fa-chart-pie"></i> prediction risk distribution\n                </h3>\n                <span class="badge bg-light text-dark border">30 days</span>\n              </div>\n\n              <div style="position: relative; height: 300px; width: 100%;">\n                <canvas id="riskdistributionchartcanvas"></canvas>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n        <!-- recent predictions table card -->\n        <div class="card-master mb-4">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-list-check"></i> recent predictions\n            </h3>\n            <a href="/prediction-history" class="btn btn-link btn-sm text-decoration-none fw-semibold">\n              view all predictions \xe2\x86\x92\n            </a>\n          </div>\n\n          <div class="table-responsive">\n            <table class="custom-table">\n              <thead>\n                <tr>\n                  <th>date</th>\n                  <th>risk level</th>\n                  <th>risk score</th>\n                  <th>status</th>\n                </tr>\n              </thead>\n              <tbody>\n                <tr>\n                  <td>13 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">18%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>11 aug 2026</td>\n                  <td><span class="badge-risk-medium"><i class="fa-solid fa-circle text-warning fs-8"></i> medium</span></td>\n                  <td class="fw-bold text-warning">54%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n                <tr>\n                  <td>08 aug 2026</td>\n                  <td><span class="badge-risk-low"><i class="fa-solid fa-circle text-success fs-8"></i> low</span></td>\n                  <td class="fw-bold text-success">21%</td>\n                  <td><span class="badge bg-light text-dark border">completed</span></td>\n                </tr>\n              </tbody>\n            </table>\n          </div>\n        </div>\n\n        <!-- quick actions section -->\n        <div class="card-master">\n          <div class="card-header-master">\n            <h3 class="card-title-master">\n              <i class="fa-solid fa-bolt"></i> quick actions\n            </h3>\n          </div>\n\n          <div class="row g-3">\n            <div class="col-sm-6 col-md-3">\n              <a href="/daily-monitoring" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-notes-medical"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">daily health monitoring</div>\n                  <div class="quick-action-sub">record health metrics</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/prediction-history" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-clock-rotate-left"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">prediction history</div>\n                  <div class="quick-action-sub">view past assessments</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/weekly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-week"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">weekly summary</div>\n                  <div class="quick-action-sub">7-day trends & load</div>\n                </div>\n              </a>\n            </div>\n\n            <div class="col-sm-6 col-md-3">\n              <a href="/monthly-summary" class="quick-action-card">\n                <div class="quick-action-icon">\n                  <i class="fa-solid fa-calendar-days"></i>\n                </div>\n                <div>\n                  <div class="quick-action-title">monthly summary</div>\n                  <div class="quick-action-sub">30-day risk analysis</div>\n                </div>\n              </a>\n            </div>\n          </div>\n        </div>\n\n      </div>\n\n    </main>\n  </div>\n\n</div>\n\n\n  <!-- bootstrap 5 js bundle -->\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n\n  <!-- master ui js -->\n  <script src="/static/js/main.js"></script>\n\n  \n<script src="/static/js/dashboard.js"></script>\n\n</body>\n</html>'

```

### BUG-020: `test_summaries.TestSummaries.test_monthly_summary_empty`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 65, in test_monthly_summary_empty
    self.assertEqual(data['total_records'], 0)
                     ~~~~^^^^^^^^^^^^^^^^^
KeyError: 'total_records'

```

### BUG-021: `test_summaries.TestSummaries.test_summary_user_isolation`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 109, in test_summary_user_isolation
    db.session.commit()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO daily_health_records (user_id, record_date, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury, injury_details, risk_score, risk_label, review_status, reviewed_by, reviewed_at, created_at) VALUES (%(user_id)s, %(record_date)s, %(sleep_hours)s, %(training_hours)s, %(resting_heart_rate)s, %(fatigue_level)s, %(stress_level)s, %(previous_injury)s, %(injury_details)s, %(risk_score)s, %(risk_label)s, %(review_status)s, %(reviewed_by)s, %(reviewed_at)s, %(created_at)s)]
[parameters: {'user_id': 444, 'record_date': '2026-09-24', 'sleep_hours': 5.0, 'training_hours': 6.0, 'resting_heart_rate': 90, 'fatigue_level': 8, 'stress_level': 8, 'previous_injury': 0, 'injury_details': None, 'risk_score': 85.0, 'risk_label': 'High Risk', 'review_status': 'Pending Review', 'reviewed_by': None, 'reviewed_at': None, 'created_at': datetime.datetime(2026, 9, 24, 4, 1, 18, 364995)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-022: `test_summaries.TestSummaries.test_summary_user_isolation`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 41, in tearDown
    DailyHealthRecord.query.filter(DailyHealthRecord.user_id.in_([self.athlete_a.id, self.athlete_b.id])).delete(synchronize_session=False)
                                                                  ^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 569, in __get__
    return self.impl.get(state, dict_)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1096, in get
    value = self._fire_loader_callables(state, key, passive)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1126, in _fire_loader_callables
    return state._load_expired(state, passive)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state.py", line 828, in _load_expired
    self.manager.expired_attribute_loader(self, toload, passive)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 1674, in load_scalar_attributes
    result = load_on_ident(
        session,
    ...<4 lines>...
        no_autoflush=no_autoflush,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 510, in load_on_ident
    return load_on_pk_identity(
        session,
    ...<11 lines>...
        is_user_refresh=is_user_refresh,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 695, in load_on_pk_identity
    session.execute(
    ~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<2 lines>...
        bind_arguments=bind_arguments,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2261, in _execute_internal
    conn = self._connection_for_bind(bind)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2113, in _connection_for_bind
    return trans._connection_for_bind(engine, execution_options)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in _connection_for_bind
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 101, in _go
    self._raise_for_prerequisite_state(fn.__name__, current_state)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 975, in _raise_for_prerequisite_state
    raise sa_exc.PendingRollbackError(
    ...<6 lines>...
    )
sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO daily_health_records (user_id, record_date, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury, injury_details, risk_score, risk_label, review_status, reviewed_by, reviewed_at, created_at) VALUES (%(user_id)s, %(record_date)s, %(sleep_hours)s, %(training_hours)s, %(resting_heart_rate)s, %(fatigue_level)s, %(stress_level)s, %(previous_injury)s, %(injury_details)s, %(risk_score)s, %(risk_label)s, %(review_status)s, %(reviewed_by)s, %(reviewed_at)s, %(created_at)s)]
[parameters: {'user_id': 444, 'record_date': '2026-09-24', 'sleep_hours': 5.0, 'training_hours': 6.0, 'resting_heart_rate': 90, 'fatigue_level': 8, 'stress_level': 8, 'previous_injury': 0, 'injury_details': None, 'risk_score': 85.0, 'risk_label': 'High Risk', 'review_status': 'Pending Review', 'reviewed_by': None, 'reviewed_at': None, 'created_at': datetime.datetime(2026, 9, 24, 4, 1, 18, 364995)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8) (Background on this error at: https://sqlalche.me/e/20/7s2a)

```

### BUG-023: `test_summaries.TestSummaries.test_weekly_summary_empty`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 56, in test_weekly_summary_empty
    self.assertEqual(data['total_records'], 0)
                     ~~~~^^^^^^^^^^^^^^^^^
KeyError: 'total_records'

```

### BUG-024: `test_summaries.TestSummaries.test_weekly_summary_with_records`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 84, in test_weekly_summary_with_records
    db.session.commit()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO daily_health_records (user_id, record_date, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury, injury_details, risk_score, risk_label, review_status, reviewed_by, reviewed_at, created_at) VALUES (%(user_id)s, %(record_date)s, %(sleep_hours)s, %(training_hours)s, %(resting_heart_rate)s, %(fatigue_level)s, %(stress_level)s, %(previous_injury)s, %(injury_details)s, %(risk_score)s, %(risk_label)s, %(review_status)s, %(reviewed_by)s, %(reviewed_at)s, %(created_at)s)]
[parameters: {'user_id': 447, 'record_date': '2026-09-24', 'sleep_hours': 8.0, 'training_hours': 2.0, 'resting_heart_rate': 60, 'fatigue_level': 2, 'stress_level': 2, 'previous_injury': 0, 'injury_details': None, 'risk_score': 20.0, 'risk_label': 'Low Risk', 'review_status': 'Pending Review', 'reviewed_by': None, 'reviewed_at': None, 'created_at': datetime.datetime(2026, 9, 24, 4, 2, 10, 894634)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-025: `test_summaries.TestSummaries.test_weekly_summary_with_records`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_summaries.py", line 41, in tearDown
    DailyHealthRecord.query.filter(DailyHealthRecord.user_id.in_([self.athlete_a.id, self.athlete_b.id])).delete(synchronize_session=False)
                                                                  ^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 569, in __get__
    return self.impl.get(state, dict_)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1096, in get
    value = self._fire_loader_callables(state, key, passive)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\attributes.py", line 1126, in _fire_loader_callables
    return state._load_expired(state, passive)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state.py", line 828, in _load_expired
    self.manager.expired_attribute_loader(self, toload, passive)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 1674, in load_scalar_attributes
    result = load_on_ident(
        session,
    ...<4 lines>...
        no_autoflush=no_autoflush,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 510, in load_on_ident
    return load_on_pk_identity(
        session,
    ...<11 lines>...
        is_user_refresh=is_user_refresh,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\loading.py", line 695, in load_on_pk_identity
    session.execute(
    ~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<2 lines>...
        bind_arguments=bind_arguments,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2373, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2261, in _execute_internal
    conn = self._connection_for_bind(bind)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2113, in _connection_for_bind
    return trans._connection_for_bind(engine, execution_options)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in _connection_for_bind
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 101, in _go
    self._raise_for_prerequisite_state(fn.__name__, current_state)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 975, in _raise_for_prerequisite_state
    raise sa_exc.PendingRollbackError(
    ...<6 lines>...
    )
sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO daily_health_records (user_id, record_date, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury, injury_details, risk_score, risk_label, review_status, reviewed_by, reviewed_at, created_at) VALUES (%(user_id)s, %(record_date)s, %(sleep_hours)s, %(training_hours)s, %(resting_heart_rate)s, %(fatigue_level)s, %(stress_level)s, %(previous_injury)s, %(injury_details)s, %(risk_score)s, %(risk_label)s, %(review_status)s, %(reviewed_by)s, %(reviewed_at)s, %(created_at)s)]
[parameters: {'user_id': 447, 'record_date': '2026-09-24', 'sleep_hours': 8.0, 'training_hours': 2.0, 'resting_heart_rate': 60, 'fatigue_level': 2, 'stress_level': 2, 'previous_injury': 0, 'injury_details': None, 'risk_score': 20.0, 'risk_label': 'Low Risk', 'review_status': 'Pending Review', 'reviewed_by': None, 'reviewed_at': None, 'created_at': datetime.datetime(2026, 9, 24, 4, 2, 10, 894634)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8) (Background on this error at: https://sqlalche.me/e/20/7s2a)

```

### BUG-026: `test_team.TestTeam.test_05_athlete_joins_team_valid_code`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_team.py", line 120, in test_05_athlete_joins_team_valid_code
    self.assertEqual(res.status_code, 200)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 500 != 200

```

### BUG-027: `test_team.TestTeam.test_06_duplicate_membership_prevented`
```text
Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_team.py", line 138, in test_06_duplicate_membership_prevented
AssertionError: 500 != 400

```

### BUG-028: `test_team.TestTeam.test_07_athlete_views_my_team`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_team.py", line 149, in test_07_athlete_views_my_team
    db.session.commit()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO team_members (team_id, athlete_id, status, joined_at) VALUES (%(team_id)s, %(athlete_id)s, %(status)s, %(joined_at)s)]
[parameters: {'team_id': 60, 'athlete_id': 493, 'status': 'active', 'joined_at': datetime.datetime(2026, 9, 24, 4, 20, 19, 350049)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-029: `test_team.TestTeam.test_08_coach_views_team_members`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_team.py", line 166, in test_08_coach_views_team_members
    db.session.commit()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO team_members (team_id, athlete_id, status, joined_at) VALUES (%(team_id)s, %(athlete_id)s, %(status)s, %(joined_at)s)]
[parameters: {'team_id': 61, 'athlete_id': 496, 'status': 'active', 'joined_at': datetime.datetime(2026, 9, 24, 4, 21, 10, 820581)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

### BUG-030: `test_team.TestTeam.test_09_coach_removes_athlete_preserves_data`
```text
Traceback (most recent call last):
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (1205, 'Lock wait timeout exceeded; try restarting transaction')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\AtheleteAI\tests\test_team.py", line 187, in test_09_coach_removes_athlete_preserves_data
    inj = Injury(user_id=self.athlete.id, injury_type="Hamstring Strain", body_part="Thigh", injury_date="2026-08-01", severity="Mild", recovery_status="Recovered")
    ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\scoping.py", line 596, in commit
    return self._proxied.commit()
           ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 2035, in commit
    trans.commit(_to_root=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "<string>", line 2, in commit
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1316, in commit
    self._prepare_impl()
    ~~~~~~~~~~~~~~~~~~^^
  File "<string>", line 2, in _prepare_impl
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\state_changes.py", line 137, in _go
    ret_value = fn(self, *arg, **kw)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 1290, in _prepare_impl
    self.session.flush()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4353, in flush
    self._flush(objects)
    ~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4488, in _flush
    with util.safe_reraise():
         ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\session.py", line 4449, in _flush
    flush_context.execute()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 465, in execute
    rec.execute(self)
    ~~~~~~~~~~~^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\unitofwork.py", line 641, in execute
    util.preloaded.orm_persistence.save_obj(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.mapper,
        ^^^^^^^^^^^^
        uow.states_for_mapper_hierarchy(self.mapper, False, False),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        uow,
        ^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 94, in save_obj
    _emit_insert_statements(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        base_mapper,
        ^^^^^^^^^^^^
    ...<3 lines>...
        insert,
        ^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\orm\persistence.py", line 1234, in _emit_insert_statements
    result = connection.execute(
        statement,
        params,
        execution_options=execution_options,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1421, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\sql\elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1643, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 153, in execute
    result = self._query(query)
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\cursors.py", line 322, in _query
    conn.query(q)
    ~~~~~~~~~~^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 575, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
                          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 826, in _read_query_result
    result.read()
    ~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 1203, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\connections.py", line 782, in _read_packet
    packet.raise_for_error()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\protocol.py", line 219, in raise_for_error
    err.raise_mysql_exception(self._data)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\jithi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1205, 'Lock wait timeout exceeded; try restarting transaction')
[SQL: INSERT INTO daily_health_records (user_id, record_date, sleep_hours, training_hours, resting_heart_rate, fatigue_level, stress_level, previous_injury, injury_details, risk_score, risk_label, review_status, reviewed_by, reviewed_at, created_at) VALUES (%(user_id)s, %(record_date)s, %(sleep_hours)s, %(training_hours)s, %(resting_heart_rate)s, %(fatigue_level)s, %(stress_level)s, %(previous_injury)s, %(injury_details)s, %(risk_score)s, %(risk_label)s, %(review_status)s, %(reviewed_by)s, %(reviewed_at)s, %(created_at)s)]
[parameters: {'user_id': 499, 'record_date': '2026-09-20', 'sleep_hours': 8.0, 'training_hours': 2.0, 'resting_heart_rate': 60, 'fatigue_level': 2, 'stress_level': 2, 'previous_injury': 0, 'injury_details': None, 'risk_score': 15.0, 'risk_label': 'Low Risk', 'review_status': 'Pending Review', 'reviewed_by': None, 'reviewed_at': None, 'created_at': datetime.datetime(2026, 9, 24, 4, 22, 2, 319331)}]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```

