"""
Singleton Design Pattern Implementation

This module demonstrates the Singleton pattern using a metaclass approach.
The Singleton pattern ensures that a class has only one instance and provides
a global point of access to that instance.

Key Components:
- Singleton Metaclass: SingletonType controls instance creation
- Singleton Class: URLFetcher ensures only one fetcher exists
- Instance Registry: Maintains single instances per class type

Use Cases:
- Database connections
- Logging services
- Configuration managers
- Resource managers (file handlers, network connections)
- Caching systems

Benefits:
- Controlled access to sole instance
- Reduced memory footprint
- Global state management
- Lazy initialization support

Drawbacks:
- Can make unit testing difficult
- May introduce global state issues
- Can violate Single Responsibility Principle
"""

import urllib.request
from typing import Dict, Any, Type


class SingletonType(type):
    """
    Singleton Metaclass - controls class instantiation to ensure uniqueness.
    
    This metaclass overrides the __call__ method to intercept object creation.
    It maintains a registry of instances and returns the existing instance
    if one already exists for the class.
    """

    # Class-level registry to store singleton instances
    _instances: Dict[Type[Any], Any] = {}

    def __call__(cls: Type[Any], *args: Any, **kwargs: Any) -> Any:
        """
        Override object creation to implement singleton behavior.
        
        Args:
            cls: The class being instantiated
            *args: Positional arguments for the constructor
            **kwargs: Keyword arguments for the constructor
            
        Returns:
            The single instance of the class (existing or newly created)
        """
        # Check if instance already exists for this class
        if cls not in cls._instances:
            # Create new instance using the parent metaclass
            obj = type.__call__(cls, *args, **kwargs)
            # Store the instance in our registry
            cls._instances[cls] = obj

        # Return the singleton instance
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    """
    Concrete Singleton class for fetching and storing web content.
    
    This class demonstrates the Singleton pattern by ensuring only one
    URL fetcher exists in the application. It maintains a list of
    successfully fetched URLs and appends content to a single file.
    """

    def __init__(self) -> None:
        """
        Initialize the URL fetcher.
        
        Note: This will only be called once due to the Singleton pattern,
        even if URLFetcher() is called multiple times.
        """
        self.urls: list[str] = []  # Track successfully fetched URLs
        print(f"URLFetcher instance created (ID: {id(self)})")

    def fetch(self, url: str) -> None:
        """
        Fetch content from a URL and save it to a file.
        
        Args:
            url: The URL to fetch content from
            
        Note:
            Only successful fetches (HTTP 200) are saved and tracked.
            All content is appended to the same 'content.html' file.
        """
        try:
            print(f"Fetching: {url}")
            req = urllib.request.Request(url)

            with urllib.request.urlopen(req) as response:
                if response.code == 200:
                    page_content = response.read()

                    # Append content to shared file (singleton behavior)
                    with open("content.html", "a", encoding="utf-8") as f:
                        f.write(f"\n\n<!-- Content from {url} -->\n")
                        f.write(str(page_content))

                    # Track successful fetch
                    self.urls.append(url)
                    print(f"✓ Successfully fetched: {url}")
                else:
                    print(f"✗ Failed to fetch {url}: HTTP {response.code}")

        except Exception as e:
            print(f"✗ Error fetching {url}: {e}")


def main() -> None:
    """
    Demonstrate the Singleton pattern with URL fetching.
    
    Shows that multiple calls to URLFetcher() return the same instance
    and that state is shared across all references to the singleton.
    """
    print("=== Singleton Pattern Demonstration ===\n")

    # URLs to fetch for demonstration
    my_urls: list[str] = [
        "http://python.org",
        "https://planetpython.org/", 
        "https://djangoproject.com/",
    ]

    # Demonstrate singleton behavior
    print("Testing singleton behavior:")
    fetcher1 = URLFetcher()
    fetcher2 = URLFetcher()

    # Both variables should reference the same object
    print(f"fetcher1 is fetcher2: {fetcher1 is fetcher2}")
    print(f"fetcher1 ID: {id(fetcher1)}")
    print(f"fetcher2 ID: {id(fetcher2)}")
    print()

    # Use the singleton to fetch URLs
    print("Fetching URLs using singleton instance:")
    for url in my_urls:
        fetcher1.fetch(url)  # Could use fetcher1 or fetcher2 - same object

    # Show shared state
    print(f"\nURLs fetched by singleton: {fetcher1.urls}")
    print(f"Total URLs processed: {len(fetcher1.urls)}")

    # Verify state is shared
    print(f"\nState verification:")
    print(f"fetcher1.urls == fetcher2.urls: {fetcher1.urls == fetcher2.urls}")


if __name__ == "__main__":
    # main()
