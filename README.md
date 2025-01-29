# AI Nexus

This project is a Python-based script that dynamically generates HTML pages to showcase AI tools categorized into various fields, such as Automation, Development, Visuals, and more. The website utilises **Tailwind CSS** for styling and **FontAwesome** for icons.

---

## Features

- **Dynamic HTML Generation:** Automatically generates a `index.html` file listing all AI tool categories with descriptions and images.
- **SEO-Friendly:** Includes meta tags (description, keywords, Open Graph, Twitter cards) for better search engine optimization.
- **Responsive Design:** Uses Tailwind CSS to ensure the website looks great on all screen sizes.
- **Category Pages:** Individual HTML pages are generated for each category with AI tools listed under them.
- **Custom Styling:** Gradient backgrounds, hover animations, and rounded card designs enhance user experience.

---

## How It Works

1. **Input:** The script reads a CSV file (`AIwebsites.csv`) containing the following columns:
   - `Product`: Name of the AI tool.
   - `URL`: Link to the AI tool.
   - `Description`: A brief description of the AI tool.
   - `Category`: The category to which the AI tool belongs.

2. **Images:** The script uses placeholder images located in the `images` directory for each category.

3. **Output:**
   - A `index.html` page listing all categories with their descriptions and images.
   - Individual category pages (`<category_name>.html`) displaying tools specific to that category.

---

## Setup

### Prerequisites
- Python 3.7+
- Required Python libraries:
  ```bash
  pip install pandas
  ```

### Folder Structure
Ensure the following structure exists:
```
.
|-- script.py          # This Python script
|-- AIwebsites.csv     # Input CSV file
|-- images/            # Folder containing placeholder images
    |-- Automation.png
    |-- Development.png
    ...
```

---

## Usage

1. **Prepare the CSV File:**
   - Ensure `AIwebsites.csv` contains the required columns: `Product`, `URL`, `Description`, `Category`.

2. **Run the Script:**
   ```bash
   python script.py
   ```

3. **Generated Output:**
   - A `index.html` file in the root directory.
   - Multiple `<category_name>.html` files for individual categories.

4. **Open in Browser:** Open `index.html` in any modern web browser to explore the AI tools.

---

## SEO Optimizations

The script generates SEO-friendly HTML by:
- Adding meta descriptions, keywords, and Open Graph tags.
- Including Twitter Card support for better social sharing.
- Using clean and descriptive URLs.

---

## Customization

- **Styling:** Update Tailwind CSS classes in the script to change the appearance.
- **Icons:** Replace FontAwesome icons in the footer or elsewhere as needed.
- **Images:** Update category placeholder images in the `images/` folder.

---

## Example Category Page

Each category page (e.g., `Automation.html`) includes:
- Header with navigation.
- Grid layout of AI tools with images, descriptions, and links.

---

## License
This project is open-source and available under the MIT License.

---

## Author
**Amit Sarkar**  
LinkedIn: [Amit Sarkar](https://www.linkedin.com/in/amitsarkar007)  
GitHub: [amitsarkar007](https://github.com/amitsarkar007)