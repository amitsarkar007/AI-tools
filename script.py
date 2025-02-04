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
  <meta name="description" content="AI Nexus is a curated hub showcasing top AI tools, categorized for easy access.">
  <meta name="keywords" content="AI tools, artificial intelligence, AI, tools, directory, AI Nexus, Nexus">
  <meta name="author" content="Amit Sarkar">
  <link rel="icon" href="images/favicon.png" type="image/x-icon">
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Nexus</title>
  <link href="{tailwind_css_link}" rel="stylesheet">
  <script type="text/javascript" src="{fontawesome_js}" crossorigin="anonymous"></script>
  <meta property="og:title" content="AI Nexus">
  <meta property="og:description" content="AI Nexus is a curated hub showcasing top AI tools, categorized for easy access.">
  <meta property="og:image" content="https://ai-nexus.tech/images/favicon.png">
  <meta property="og:url" content="https://ai-nexus.tech/">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="AI Nexus">
  <meta name="twitter:description" content="AI Nexus is a curated hub showcasing top AI tools, categorized for easy access.">
  <meta name="twitter:image" content="https://ai-nexus.tech/images/favicon.png">
  <script>
    function scrollToTop() {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}
  </script>
</head>
<body class="bg-gray-100 text-gray-900">
      
    <!-- Hero Section -->
    <section class="relative w-full h-screen flex items-center justify-center bg-cover bg-center" style="background-image: url('https://cdn.pixabay.com/photo/2022/02/15/10/35/hand-7014643_1280.jpg');">
      <div class="absolute inset-0 bg-black opacity-50"></div>
      <div class="relative z-10 flex flex-col items-center justify-center text-center text-white px-6 md:px-12">
        <div class="flex flex-wrap justify-center items-center p-6 md:p-10">
          <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold">Welcome to</h1>
          <img src="images/favicon.png" alt="AI Nexus Logo" class="w-10 h-10 sm:w-12 sm:h-12 mx-3">
          <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold">Nexus</h1>
        </div>
        <p class="text-lg sm:text-xl md:text-2xl mb-6 max-w-2xl">Your one-stop AI directory, categorized for easy access.</p>
        <a href="#categories" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300">Explore categories</a>
      </div>
    </section>

    <div class="flex flex-col items-center justify-center min-h-screen px-6">
        <!-- Main Heading -->
        <h1 id="categories" class="text-3xl md:text-4xl font-semibold text-center text-gray-800 p-16">
            One stop <span class="text-blue-500">AI directory</span>, <br> <span class="font-bold">categorized for easy access.</span>
        </h1>
        
        <!-- Features Section -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-8 max-w-6xl w-full ">
"""
# Add category cards with descriptions and images
for category, description in category_descriptions.items():
    sanitized_category = category.replace(" ", "_")
    image_path = category_images.get(category, "")
    
    categories_html += f"""
      <div class=\"bg-white p-6 rounded-2xl shadow-md text-center flex flex-col h-full hover:shadow-2xl transition-transform transform hover:scale-105\">
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
  </div>
  <!-- Testimonials Section -->
  <div class="mt-10 max-w-6xl w-full mx-auto px-4">
      <h2 class="text-2xl font-extrabold text-center text-gray-800 mb-6">What our users say</h2>
      <div class="flex flex-wrap justify-center gap-4">
          <div class="w-full sm:w-80 bg-white p-4 rounded-lg shadow-md">
              <p class="text-gray-700 italic">"AI Nexus has transformed the way I find new AI tools. Highly recommended!"</p>
              <p class="text-gray-900 font-bold mt-2">- Janki C.</p>
          </div>
          <div class="w-full sm:w-80 bg-white p-4 rounded-lg shadow-md">
              <p class="text-gray-700 italic">"Helps me search various tools easily!"</p>
              <p class="text-gray-900 font-bold mt-2">- Gaurav B.</p>
          </div>
          <div class="w-full sm:w-80 bg-white p-4 rounded-lg shadow-md">
              <p class="text-gray-700 italic">"Easy to recommend to people. One stop place for everything. Love it!"</p>
              <p class="text-gray-900 font-bold mt-2">- Rahul P.</p>
          </div>
      </div>
  </div>

  <!-- Scroll to Top Button -->
  <button onclick="scrollToTop()" class="fixed bottom-4 bg-white shadow-md right-4 text-black p-3 rounded-full shadow-x3 hover:shadow-2xl transition-transform transform hover:scale-105">
      <i class="fas fa-arrow-up"></i>
  </button>

  <!-- Footer -->
  <footer class="mt-10 text-black-900 text-sm w-full p-6 flex flex-col md:flex-row justify-between items-center">
      <div class="container mx-auto flex flex-col items-center space-y-6 md:flex-row md:justify-between px-8">
        <div class="text-center md:text-left">
          <h3 class="text-lg font-bold" style="color:black"><a href="index.html" title="AI Nexus" class="hover:opacity-80 transition">AI Nexus</a></h3>
          <ul class="mt-2 space-y-2">
            <li><a href="about.html" class="text-sm hover:opacity-80 transition">About</a></li>
            <li><a href="credit.html" class="text-sm hover:opacity-80 transition">Credit</a></li>
            <li><a href="explore.html" class="text-sm hover:opacity-80 transition">Explore AI</a></li>
          </ul>
        </div>
        <p><i class="fas fa-copyright fa-fw" style="color:black"></i> AI Nexus 2025</p>
        <div class="flex justify-center md:justify-end space-x-6">
          <a target="_blank" rel="noreferrer" href="https://linkedin.com/in/amitsarkar007" title="LinkedIn" class="hover:opacity-80 transition"><i class="fab fa-linkedin fa-fw" style="font-size:20px;color:black"></i></a>
          <a target="_blank" rel="noreferrer" href="https://x.com/amit_Sarkar007" title="X" class="hover:opacity-80 transition"><i class="fab fa-x-twitter fa-fw" style="font-size:20px;color:black"></i></a>
          <a target="_blank" rel="noreferrer" href="https://github.com/amitsarkar007" title="GitHub" class="hover:opacity-80 transition"><i class="fab fa-github fa-fw" style="font-size:20px;color:black"></i></a>
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
    function scrollToTop() {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}
  </script>
</head>
<body class="bg-gray-100 text-gray-900 flex flex-col min-h-screen">

    <!-- Heading -->
    <div class="flex justify-between items-center px-10 py-4 w-full">
      <a href="index.html"><img src="images/favicon.png" alt="AI Nexus Logo" class="w-8 h-8"></a>
      <h1 class="text-4xl font-extrabold text-green-700 text-center flex-grow">{ category }</h1>
      <div class="relative">
        <button id="dropdown-button" onclick="toggleDropdown()" class="text-green-700 text-2xl hover:opacity-80 transition"><i class="fas fa-bars"></i></button>
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
    </div>

    <!-- Main Content -->
    <div class="flex-grow flex flex-col items-center justify-center min-h-screen px-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-8 max-w-6xl w-full ">
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
          <div class="bg-white p-6 rounded-2xl shadow-md text-center flex flex-col h-full hover:shadow-2xl transition-transform transform hover:scale-105">
            <img src="{image_path}" alt="{product_name}" class="w-full h-48 object-cover rounded-t-lg">
            <div class="p-6">
              <h2 class="text-xl font-extrabold text-gray-800 tracking-wide">{product_name}</h2>
              <p class="text-gray-600 mt-2">{description}</p>
              <a href="{url}" target="_blank" class="mt-4 inline-block text-white bg-gradient-to-r from-green-600 to-green-500 hover:from-green-500 hover:to-green-400 px-4 py-2 rounded-full transition">Visit</a>
            </div>
          </div>
        """

    # Close category HTML
    category_html += """
      </div>
    </div>

  <!-- Scroll to Top Button -->
  <button onclick="scrollToTop()" class="fixed bottom-4 bg-white shadow-md right-4 text-black p-3 rounded-full shadow-x3 hover:shadow-2xl transition-transform transform hover:scale-105">
      <i class="fas fa-arrow-up"></i>
  </button>

  <!-- Footer -->
  <footer class="mt-10 text-black-900 text-sm w-full p-6 flex flex-col md:flex-row justify-between items-center">
      <div class="container mx-auto flex flex-col items-center space-y-6 md:flex-row md:justify-between px-8">
        <div class="text-center md:text-left">
          <h3 class="text-lg font-bold" style="color:black"><a href="index.html" title="AI Nexus" class="hover:opacity-80 transition">AI Nexus</a></h3>
          <ul class="mt-2 space-y-2">
            <li><a href="about.html" class="text-sm hover:opacity-80 transition">About</a></li>
            <li><a href="credit.html" class="text-sm hover:opacity-80 transition">Credit</a></li>
            <li><a href="explore.html" class="text-sm hover:opacity-80 transition">Explore AI</a></li>
          </ul>
        </div>
        <p><i class="fas fa-copyright fa-fw" style="color:black"></i> AI Nexus 2025</p>
        <div class="flex justify-center md:justify-end space-x-6">
          <a target="_blank" rel="noreferrer" href="https://linkedin.com/in/amitsarkar007" title="LinkedIn" class="hover:opacity-80 transition"><i class="fab fa-linkedin fa-fw" style="font-size:20px;color:black"></i></a>
          <a target="_blank" rel="noreferrer" href="https://x.com/amit_Sarkar007" title="X" class="hover:opacity-80 transition"><i class="fab fa-x-twitter fa-fw" style="font-size:20px;color:black"></i></a>
          <a target="_blank" rel="noreferrer" href="https://github.com/amitsarkar007" title="GitHub" class="hover:opacity-80 transition"><i class="fab fa-github fa-fw" style="font-size:20px;color:black"></i></a>
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