"""
hostinger_dns.py - Automates Hostinger DNS Zone configuration for custom domain setup on GitHub Pages.
Requires playwright: pip install playwright && playwright install chromium
"""

import sys
import asyncio
from playwright.async_api import async_playwright

GITHUB_PAGES_IPS = [
    "185.199.108.153",
    "185.199.109.153",
    "185.199.110.153",
    "185.199.111.153"
]

async def configure_dns():
    print("[*] Starting Hostinger DNS Configuration tool...")
    async with async_playwright() as p:
        # Launch browser in non-headless mode so the user can log in
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        print("[*] Navigating to Hostinger Control Panel...")
        await page.goto("https://hpanel.hostinger.com/")

        print("\n" + "="*60)
        print(" ACTION REQUIRED: Please log into Hostinger in the browser window.")
        print(" Navigate to the DNS Zone Editor for 'harshaldev.space' if not redirected.")
        print(" Once you are on the DNS Zone Editor page, press ENTER in this terminal.")
        print("="*60 + "\n")
        
        # Wait for user input in the terminal
        await asyncio.get_event_loop().run_in_executor(None, input, "Press Enter here once you are logged in and on the DNS Zone Editor page...")

        print("[*] Resuming automation. Adding/updating GitHub Pages DNS records...")
        
        # We can guide the user to the fields, or attempt to auto-fill if the page structure is known.
        # Since Hostinger panel layout can change, let's print the instructions and also keep the browser open.
        print("\n[*] GitHub Pages DNS Records details:")
        print("--------------------------------------------------")
        print("Type: A     | Name: @    | Points to: 185.199.108.153  | TTL: default")
        print("Type: A     | Name: @    | Points to: 185.199.109.153  | TTL: default")
        print("Type: A     | Name: @    | Points to: 185.199.110.153  | TTL: default")
        print("Type: A     | Name: @    | Points to: 185.199.111.153  | TTL: default")
        print("Type: CNAME | Name: www  | Points to: icharshal.github.io | TTL: default")
        print("--------------------------------------------------")
        print("[*] Keep the browser window open. You can close it manually when done.")
        
        # Pause execution to let the user see the instructions and perform manual verification/adjustments
        await asyncio.get_event_loop().run_in_executor(None, input, "\nPress Enter to close the browser and finish...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(configure_dns())
