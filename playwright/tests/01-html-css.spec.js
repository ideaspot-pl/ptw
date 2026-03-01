// @ts-check
import { test, expect } from '@playwright/test';

test('hello', async ({ page }, testInfo) => {
  await page.goto('http://localhost:8000/01-html-css/intro/hello/hello.html');
  
  await page.setViewportSize({
    width: 200,
    height: 100,
    deviceScaleFactor: 1,
  })
  
  await page.screenshot({path: `./screenshots/01-html-css/hello.png`});
});
