import sys
import asyncio
from crawl import crawl_page_async

async def main():
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    print(f"starting crawl of: {base_url}...")

    page_data = await crawl_page_async(base_url)

    print(f"Found {len(page_data)} pages:")
    for page in page_data.values():
        print(f"Found {len(page['outgoing_links'])} outgoing links on {page['url']}")

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
