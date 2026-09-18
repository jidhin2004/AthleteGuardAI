/**
 * AthleteGuard AI - Core UI Script & Navigation Handler
 */

document.addEventListener('DOMContentLoaded', function () {
  // Password Visibility Toggle Handler
  const toggleButtons = document.querySelectorAll('.password-toggle');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function () {
      const targetId = this.getAttribute('data-target');
      const input = document.getElementById(targetId);
      const icon = this.querySelector('i');

      if (input) {
        if (input.type === 'password') {
          input.type = 'text';
          icon.classList.remove('fa-eye');
          icon.classList.add('fa-eye-slash');
        } else {
          input.type = 'password';
          icon.classList.remove('fa-eye-slash');
          icon.classList.add('fa-eye');
        }
      }
    });
  });

  // Landing Page Navbar Anchor Smooth Scrolling & Active State
  const navLinks = document.querySelectorAll('.nav-link-landing');
  const navbarCollapse = document.getElementById('landingNavbarNav');

  navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const targetSection = document.querySelector(href);
        if (targetSection) {
          // Collapse navbar on mobile if open
          if (navbarCollapse && navbarCollapse.classList.contains('show')) {
            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
            if (bsCollapse) bsCollapse.hide();
          }

          const headerOffset = 80;
          const elementPosition = targetSection.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });

  // Athlete Notification Handler
  if (document.getElementById('athleteNotificationDropdown')) {
    fetchAthleteNotifications();
  }
});

// BFCache Navigation Protection: Force page reload if restored from browser memory cache (e.g. Back button)
window.addEventListener('pageshow', function (event) {
  if (event.persisted) {
    window.location.reload();
  }
});

function getCsrfToken() {
  const metaElem = document.querySelector('meta[name="csrf-token"]');
  if (metaElem) {
    return metaElem.getAttribute('content');
  }
  const inputElem = document.querySelector('input[name="csrf_token"]');
  if (inputElem) {
    return inputElem.value;
  }
  return '';
}

function fetchAthleteNotifications() {
  fetch('/api/notifications')
    .then(res => res.json())
    .then(data => {
      if (data.status !== 'success') return;

      const badge = document.getElementById('notificationBadge');
      const list = document.getElementById('notificationsList');

      if (badge) {
        if (data.unread_count > 0) {
          badge.textContent = data.unread_count;
          badge.style.display = 'inline-block';
        } else {
          badge.style.display = 'none';
        }
      }

      if (list) {
        if (!data.notifications || data.notifications.length === 0) {
          list.innerHTML = `
            <div class="text-center py-4 text-muted fs-7">
              <i class="fa-solid fa-bell-slash text-slate-300 fs-4 mb-2 d-block"></i>
              No new notifications.
            </div>`;
          return;
        }

        list.innerHTML = data.notifications.map(n => `
          <div class="p-3 mb-2 rounded-3 border ${n.is_read ? 'bg-light border-light-subtle' : 'bg-primary-subtle border-primary-subtle'}" style="transition: all 0.2s;">
            <div class="d-flex justify-content-between align-items-start gap-2 mb-1.5">
              <span class="fw-bold fs-7 ${n.is_read ? 'text-secondary' : 'text-dark'}">
                <span class="me-1">${n.is_read ? '○' : '●'}</span>
                Health Assessment Reviewed
              </span>
              <span class="fs-8 text-muted">${n.created_at_formatted}</span>
            </div>
            <p class="fs-7 text-dark mb-2" style="line-height: 1.4; background: rgba(255,255,255,0.75); padding: 8px; border-radius: 6px; border: 1px solid rgba(0,0,0,0.05);">
              <strong class="d-block text-primary fs-8 mb-1">Recommendation:</strong>
              ${escapeHtml(n.message)}
            </p>
            ${!n.is_read ? `
              <div class="text-end">
                <button type="button" class="btn btn-sm btn-outline-primary py-0 px-2 fw-semibold fs-8" onclick="markNotificationRead(${n.id})">
                  Mark as Read
                </button>
              </div>` : ''}
          </div>
        `).join('');
      }
    })
    .catch(err => console.error('Notification error:', err));
}

function markNotificationRead(id) {
  fetch(`/api/notifications/${id}/read`, {
    method: 'PUT',
    headers: { 'X-CSRFToken': getCsrfToken() }
  })
    .then(res => res.json())
    .then(data => {
      if (data.status === 'success') fetchAthleteNotifications();
    });
}

function markAllNotificationsRead(e) {
  if (e) e.preventDefault();
  fetch('/api/notifications/read-all', {
    method: 'PUT',
    headers: { 'X-CSRFToken': getCsrfToken() }
  })
    .then(res => res.json())
    .then(data => {
      if (data.status === 'success') fetchAthleteNotifications();
    });
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
