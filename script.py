import pandas as pd
import os

# Load the CSV file
csv_file = "AIwebsites.csv"
ai_tools_data = pd.read_csv(csv_file)

# Directory for images
images_dir = "images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Tailwind CSS and Font Awesome links
tailwind_css_link = "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
fontawesome_js = "https://kit.fontawesome.com/878884ebe6.js"

# Add category descriptions and generate placeholder images for each category
category_descriptions = {
    "Automation": "Tools designed to automate repetitive tasks, streamline workflows, and enhance productivity.",
    "Development": "AI-powered tools for developers to build, debug, and optimise their applications.",
    "Visuals": "Creative tools that generate high-quality images, videos, and designs with AI.",
    "Chatbot": "Conversational AI tools for communication, customer support, and automation.",
    "Ideation": "Tools that help with brainstorming, generating ideas, and enhancing creativity.",
    "Productivity": "AI tools that boost efficiency and simplify day-to-day tasks.",
    "Dictation": "Voice-to-text tools and transcription services powered by AI.",
    "Search": "Advanced AI-powered search engines and information retrieval tools.",
    "Learning": "Educational tools designed to enhance learning experiences and personalise education.",
    "Audio": "AI tools for audio processing, editing, and generation.",
    "Career": "Tools to help with career development, job searching, and skill building.",
    "Scraper": "AI-powered web scraping and data extraction tools.",
    "LLM": "Large Language Models (LLMs) for generating text and understanding natural language.",
    "Education": "AI tools and platforms to transform the way we teach and learn, offering personalised and interactive educational experiences."
}

category_images = {
    "Automation": "images/Automation.png",
    "Development": "images/Development.png",
    "Visuals": "images/Visuals.png",
    "Chatbot": "images/Chatbot.png",
    "Ideation": "images/Ideation.png",
    "Productivity": "images/Productivity.png",
    "Dictation": "images/Dictation.png",
    "Search": "images/Search.png",
    "Learning": "images/Learning.png",
    "Audio": "images/Audio.png",
    "Career": "images/Career.png",
    "Scraper": "images/Scraper.png",
    "LLM": "images/LLM.png",
    "Education": "images/Education.png"
}

# Generate index.html
categories_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="description" content="Discover the best AI tools available online, categorized for easy access.">
  <meta name="keywords" content="AI tools, artificial intelligence, AI, tools, directory">
  <meta name="author" content="Amit Sarkar">
  <link rel="icon" href="images/favicon.png" type="image/x-icon">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Hub</title>
  <link href="{tailwind_css_link}" rel="stylesheet">
  <script type="text/javascript" src="{fontawesome_js}" crossorigin="anonymous"></script>
  <meta property="og:title" content="AI Hub">
  <meta property="og:description" content="Discover the best AI tools available online, categorized for easy access.">
  <meta property="og:image" content="images/favicon.png">
  <meta property="og:url" content="https://yourdomain.ai">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="AI Hub">
  <meta name="twitter:description" content="Discover the best AI tools available online, categorized for easy access.">
  <meta name="twitter:image" content="images/favicon.png">
</head>
<body class="bg-gray-50 font-sans flex flex-col min-h-screen">
  <header class="bg-gradient-to-r from-blue-700 to-blue-500 text-white py-6 shadow-lg text-center rounded-b-lg drop-shadow-md">
    <h1 class="text-4xl font-extrabold tracking-wide drop-shadow-md">AI Hub</h1>
  </header>
  <main class="p-8 flex-grow">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
"""

# Add category cards with descriptions and images
for category, description in category_descriptions.items():
    sanitized_category = category.replace(" ", "_")
    image_path = category_images.get(category, "")
    
    categories_html += f"""
      <div class=\"bg-white rounded-lg shadow-lg hover:shadow-2xl transition-transform transform hover:scale-105 overflow-hidden border border-gray-200\">
        <img src=\"{image_path}\" alt=\"{category}\" class=\"w-full h-48 object-cover rounded-t-lg\">
        <div class=\"p-6 text-center\">
          <h2 class=\"text-xl font-extrabold text-gray-800 tracking-wide\">{category}</h2>
          <p class=\"text-gray-600 mt-2\">{description}</p>
          <a href=\"{sanitized_category}.html\" class=\"mt-4 inline-block text-white bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 px-4 py-2 rounded-full transition\">Explore</a>
        </div>
      </div>
    """

# Close index.html
categories_html += """
    </div>
  </main>
  <footer class="bg-gray-900 text-white py-8 rounded-t-lg drop-shadow-md">
    <div class="container mx-auto text-center">
        <p class="text-sm">All Rights Reserved • <i class="fas fa-copyright fa-fw" style="color:white"></i>Amit Sarkar 2025 • Powered by <a target="_blank" rel="noreferrer" class="hover:opacity-80 transition" href="https://tailwindcss.com/" title="Open Tailwind CSS website">Tailwind CSS</a></p>
        <div class="flex justify-center space-x-6 mt-4">
            <a target="_blank" rel="noreferrer" href="https://www.linkedin.com/in/amitsarkar007" title="LinkedIn" class="hover:opacity-80 transition"><i class="fab fa-linkedin fa-fw" style="font-size:20px;color:white"></i></a>
            <a target="_blank" rel="noreferrer" href="https://twitter.com/amit_Sarkar007" title="Twitter" class="hover:opacity-80 transition"><i class="fab fa-twitter fa-fw" style="font-size:20px;color:white"></i></a>
            <a target="_blank" rel="noreferrer" href="https://github.com/amitsarkar007" title="GitHub" class="hover:opacity-80 transition"><i class="fab fa-github fa-fw" style="font-size:20px;color:white"></i></a>
        </div>
    </div>
  </footer>
</body>
</html>
"""

# Save index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(categories_html)

print("Generated index.html successfully!")

# Generate individual category pages
for category in category_descriptions.keys():  # Use the keys from category_descriptions
    sanitized_category = category.replace(" ", "_")
    category_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="author" content="Amit Sarkar">
  <link rel="icon" href="images/favicon.png" type="image/x-icon">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{category}</title>
  <link href="{tailwind_css_link}" rel="stylesheet">
  <script type="text/javascript" src="{fontawesome_js}" crossorigin="anonymous"></script>
  <script>
    // Toggle dropdown menu visibility
    function toggleDropdown() {{
      const menu = document.querySelector('#dropdown-menu');
      menu.classList.toggle('hidden');
    }}
    // Close dropdown if clicked outside
    document.addEventListener('click', function(event) {{
      const menu = document.querySelector('#dropdown-menu');
      const button = document.querySelector('#dropdown-button');
      if (menu && !button.contains(event.target) && !menu.contains(event.target)) {{
        menu.classList.add('hidden');
      }}
    }});
  </script>
</head>
<body class="bg-gray-50 font-sans flex flex-col min-h-screen">
  <header class="bg-gradient-to-r from-blue-700 to-blue-500 text-white py-6 shadow-lg flex justify-between items-center px-8 rounded-b-lg drop-shadow-md">
    <a href="index.html" class="text-white text-2xl hover:opacity-80 transition"><i class="fas fa-home"></i></a>
    <h1 class="text-4xl font-extrabold tracking-wide drop-shadow-md">{category}</h1>
    <div class="relative">
      <button id="dropdown-button" onclick="toggleDropdown()" class="text-white text-2xl hover:opacity-80 transition"><i class="fas fa-bars"></i></button>
      <ul id="dropdown-menu" class="absolute hidden bg-white text-gray-800 shadow-lg rounded mt-2 z-10 w-48 right-0 border border-gray-300">
"""

    # Add links to navigate to other categories
    for other_category in category_descriptions.keys():
        if other_category != category:
            sanitized_other_category = other_category.replace(" ", "_")
            category_html += f"<li class='border-b border-gray-200'><a href='{sanitized_other_category}.html' class='block px-4 py-2 hover:bg-gray-100 transition'>{other_category}</a></li>"

    category_html += """
      </ul>
    </div>
  </header>
  <main class="p-8 flex-grow">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
"""

    # Filter tools by category
    category_tools = ai_tools_data[ai_tools_data['Category'] == category]

    # Add tools to the category page
    for _, row in category_tools.iterrows():
        product_name = row['Product']
        url = row['URL']
        description = row['Description']
        sanitized_image_name = product_name.replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the image exists
        image_path = os.path.join(images_dir, f"{sanitized_image_name}.png")
        if not os.path.exists(image_path):
            print(f"Warning: Image for {product_name} not found. Skipping...")
            continue

        category_html += f"""
          <div class="bg-white rounded-lg shadow-lg hover:shadow-2xl transition-transform transform hover:scale-105 overflow-hidden">
            <img src="{image_path}" alt="{product_name}" class="w-full h-48 object-cover">
            <div class="p-6">
              <h2 class="text-xl font-extrabold text-gray-800 tracking-wide">{product_name}</h2>
              <p class="text-gray-600 mt-2">{description}</p>
              <a href="{url}" target="_blank" class="mt-6 inline-block text-white bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-500 hover:to-blue-400 px-4 py-2 rounded-full transition">Visit</a>
            </div>
          </div>
        """

    # Close category HTML
    category_html += """
    </div>
  </main>
  <footer class="bg-gray-900 text-white py-8 rounded-t-lg drop-shadow-md">
    <div class="container mx-auto text-center">
        <p class="text-sm">All Rights Reserved • <i class="fas fa-copyright fa-fw" style="color:white"></i>Amit Sarkar 2025 • Powered by <a target="_blank" rel="noreferrer" class="hover:opacity-80 transition" href="https://tailwindcss.com/" title="Open Tailwind CSS website">Tailwind CSS</a></p>
        <div class="flex justify-center space-x-6 mt-4">
            <a target="_blank" rel="noreferrer" href="https://www.linkedin.com/in/amitsarkar007" title="LinkedIn" class="hover:opacity-80 transition"><i class="fab fa-linkedin fa-fw" style="font-size:20px;color:white"></i></a>
            <a target="_blank" rel="noreferrer" href="https://twitter.com/amit_Sarkar007" title="Twitter" class="hover:opacity-80 transition"><i class="fab fa-twitter fa-fw" style="font-size:20px;color:white"></i></a>
            <a target="_blank" rel="noreferrer" href="https://github.com/amitsarkar007" title="GitHub" class="hover:opacity-80 transition"><i class="fab fa-github fa-fw" style="font-size:20px;color:white"></i></a>
        </div>
    </div>
  </footer>
</body>
</html>
"""

    # Save category HTML file
    with open(f"{sanitized_category}.html", "w", encoding="utf-8") as f:
        f.write(category_html)

    print(f"Generated {sanitized_category}.html successfully!")