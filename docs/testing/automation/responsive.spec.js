#!/usr/bin/env node
/**
 * FamilyConnect - Playwright Responsive Tests (NFR-01)
 * =====================================================
 * Test responsive design on 3 breakpoints:
 *   - Desktop:  1440x900
 *   - Tablet:   768x1024
 *   - Mobile:   375x667
 *
 * Usage:
 *   npm install -D @playwright/test
 *   npx playwright test --config=playwright.config.js responsive.spec.js
 */

const { test, expect } = require('@playwright/test');

const BREAKPOINTS = [
  { name: 'Desktop 1440', width: 1440, height: 900 },
  { name: 'Tablet 768', width: 768, height: 1024 },
  { name: 'Mobile 375', width: 375, height: 667 },
];

const PAGES = [
  { name: 'Login', path: '/login' },
  { name: 'Register', path: '/register' },
  { name: 'Dashboard', path: '/dashboard' },
  { name: 'Family Tree', path: '/family/tree' },
  { name: 'Community', path: '/community' },
  { name: 'Directory', path: '/directory' },
  { name: 'Events', path: '/events' },
];

for (const bp of BREAKPOINTS) {
  for (const page of PAGES) {
    test(`NFR-01: ${page.name} on ${bp.name}`, async ({ page: browserPage }) => {
      await browserPage.setViewportSize({ width: bp.width, height: bp.height });

      // Go to the page (mock login if needed)
      await browserPage.goto(`http://localhost:3000${page.path}`);

      // Check 1: No horizontal scroll
      const hasHorizontalScroll = await browserPage.evaluate(() => {
        return document.documentElement.scrollWidth > document.documentElement.clientWidth;
      });
      expect(hasHorizontalScroll).toBe(false);

      // Check 2: Body is visible
      const bodyVisible = await browserPage.isVisible('body');
      expect(bodyVisible).toBe(true);

      // Check 3: No layout overflow
      const overflowElements = await browserPage.evaluate(() => {
        const wide = [];
        document.querySelectorAll('*').forEach((el) => {
          const rect = el.getBoundingClientRect();
          if (rect.right > window.innerWidth + 5) {
            wide.push(el.className || el.tagName);
          }
        });
        return wide;
      });
      expect(overflowElements.length).toBe(0);
    });
  }
}

// Specific interaction tests
test('NFR-01: Mobile - hamburger menu works', async ({ page: browserPage }) => {
  await browserPage.setViewportSize({ width: 375, height: 667 });
  await browserPage.goto('http://localhost:3000/dashboard');

  // Check hamburger button present on mobile
  const hamburger = browserPage.locator('[data-testid="hamburger-menu"]');
  if (await hamburger.count() > 0) {
    await hamburger.click();
    // Navigation menu should be visible
    await expect(browserPage.locator('[data-testid="mobile-nav"]')).toBeVisible();
  }
});

test('NFR-01: Touch target size >= 44px on mobile', async ({ page: browserPage }) => {
  await browserPage.setViewportSize({ width: 375, height: 667 });
  await browserPage.goto('http://localhost:3000/login');

  // Check primary buttons
  const buttons = browserPage.locator('button');
  const count = await buttons.count();
  for (let i = 0; i < Math.min(count, 10); i++) {
    const box = await buttons.nth(i).boundingBox();
    if (box) {
      expect(box.height).toBeGreaterThanOrEqual(44);
    }
  }
});

// Cross-browser test
test.describe('NFR-01: Cross-browser', () => {
  // Configure browsers in playwright.config.js
  test('Login page renders on all configured browsers', async ({ browserPage }) => {
    await browserPage.goto('http://localhost:3000/login');
    await expect(browserPage.locator('input[type="email"]')).toBeVisible();
    await expect(browserPage.locator('input[type="password"]')).toBeVisible();
  });
});