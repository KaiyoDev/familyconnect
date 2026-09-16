import { test, expect } from '@playwright/test'

test('landing page exposes the main public entry points', async ({ page }) => {
  await page.goto('/')

  await expect(page).toHaveTitle(/FamilyConnect/i)
  await expect(page.getByRole('heading', { level: 1, name: /Kết nối gia đình/i })).toBeVisible()
  await expect(page.getByRole('link', { name: 'Đăng nhập' }).first()).toBeVisible()
  await expect(page.getByRole('link', { name: 'Khởi tạo' }).first()).toBeVisible()
})

test('unauthenticated users are redirected from the dashboard to login', async ({ page }) => {
  await page.goto('/dashboard')

  await expect(page).toHaveURL(/\/login$/)
  await expect(page.getByRole('heading', { name: 'Đăng nhập' })).toBeVisible()
  await expect(page.getByLabel('Email')).toBeVisible()
  await expect(page.getByLabel('Mật khẩu')).toBeVisible()
})