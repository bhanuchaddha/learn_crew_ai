# Working with Knowledge Sources in CrewAI

This tutorial demonstrates how to use different knowledge sources in CrewAI to process and analyze data from various file formats.

## Key Concepts

1. **Multiple File Format Support**
   - Using Docling for reading various file types including:
     - PDF, DOCX, PPTX, XLSX
     - Images, HTML
     - AsciiDoc & Markdown

2. **Knowledge Management**
   - Knowledge can be applied at Agent or Crew level
   - Knowledge configuration supports customizable embedding and chunking
   - Knowledge can be reset when needed
   - Knowledge folder should be at root level for better organization

## Implementation Overview

The example code demonstrates:
- Reading data from multiple file types (JSON, TXT, XLSX)
- Creating an agent with multiple knowledge sources
- Querying the knowledge base using natural language questions

## Code Structure
```python
# Creating knowledge sources
json_source = JSONKnowledgeSource(file_paths=["customer.json"])
txt_source = TextFileKnowledgeSource(file_paths=["products.txt"])
docling_source = CrewDoclingSource(file_paths=["transactions.xlsx"])

# Creating agent with knowledge sources
knowledge_gathering_agent = Agent(
    knowledge_sources=[json_source, txt_source, docling_source],
    # ... other configurations
)
```

## Example Outputs

Below are example queries and their results when running the knowledge gathering system:

# Output
```
# Agent: Knowledge Gatherer
## Task: Answer the quesotion using knowledge gathered How many customers are there?


# Agent: Knowledge Gatherer
## Final Answer: 
Based on the available customer data, there are a total of 3 customers. Their details are as follows:

1. **Customer ID:** 1  
   - **First Name:** John  
   - **Last Name:** Doe  
   - **Email:** john.doe@example.com  
   - **Phone:** 555-1234  
   - **Address:** 123 Elm St, Springfield, IL, 62701  
   - **Joined Date:** 2023-01-15  

2. **Customer ID:** 2  
   - **First Name:** Jane  
   - **Last Name:** Smith  
   - **Email:** jane.smith@example.com  
   - **Phone:** 555-5678  
   - **Address:** 456 Oak St, Springfield, IL, 62702  
   - **Joined Date:** 2023-02-10  

3. **Customer ID:** 3  
   - **First Name:** Emily  
   - **Last Name:** Johnson  
   - **Email:** emily.johnson@example.com  
   - **Phone:** 555-8765  
   - **Address:** 789 Pine St, Springfield, IL, 62703  
   - **Joined Date:** 2023-03-05  

This information confirms that the total count of customers is 3.


# Agent: Knowledge Gatherer
## Task: Answer the quesotion using knowledge gathered How many products are there?


# Agent: Knowledge Gatherer
## Final Answer: 
There are a total of 6 products available. 

1. **Wireless Mouse**  
   - **Product ID:** 101  
   - **Category:** Electronics  
   - **Price:** $29.99  
   - **Stock:** 150  
   - **Description:** A smooth and responsive wireless mouse.

2. **Bluetooth Headphones**  
   - **Product ID:** 102  
   - **Category:** Electronics  
   - **Price:** $49.99  
   - **Stock:** 75  
   - **Description:** High-quality sound with noise cancellation.

3. **LED Monitor**  
   - **Product ID:** 103  
   - **Category:** Electronics  
   - **Price:** $199.99  
   - **Stock:** 50  
   - **Description:** 27-inch 4K LED monitor for stunning visuals.

4. **Running Shoes**  
   - **Product ID:** 201  
   - **Category:** Footwear  
   - **Price:** $79.99  
   - **Stock:** 100  
   - **Description:** Comfortable running shoes suitable for all terrains.

5. **Leather Wallet**  
   - **Product ID:** 202  
   - **Category:** Accessories  
   - **Price:** $39.99  
   - **Stock:** 200  
   - **Description:** Genuine leather wallet with multiple compartments.

6. **Sunglasses**  
   - **Product ID:** 203  
   - **Category:** Accessories  
   - **Price:** $19.99  
   - **Stock:** 300  
   - **Description:** Stylish sunglasses for UV protection. 

These products cover various categories, including Electronics, Footwear, and Accessories.


# Agent: Knowledge Gatherer
## Task: Answer the quesotion using knowledge gathered How many products each customer bought, and what was the total cost for each customer?


# Agent: Knowledge Gatherer
## Final Answer: 
To determine how many products each customer bought and the total cost incurred, we analyze the given transactions. Below is the breakdown for each customer:

1. **Customer ID: 1**  
   - **Name:** John Doe  
   - **Products Bought:**  
     - Wireless Mouse (Product ID: 101)  
       - Quantity: 1  
       - Total Cost: 1 * $29.99 = $29.99  
     - Sunglasses (Product ID: 203)  
       - Quantity: 1  
       - Total Cost: 1 * $19.99 = $19.99  
   - **Total Products Bought:** 2  
   - **Total Cost:** $29.99 + $19.99 = $49.98  

2. **Customer ID: 2**  
   - **Name:** Jane Smith  
   - **Products Bought:**  
     - Leather Wallet (Product ID: 202)  
       - Quantity: 2  
       - Total Cost: 2 * $39.99 = $79.98  
   - **Total Products Bought:** 1  
   - **Total Cost:** $79.98  

3. **Customer ID: 3**  
   - **Name:** Emily Johnson  
   - **Products Bought:**  
     - LED Monitor (Product ID: 103)  
       - Quantity: 1  
       - Total Cost: 1 * $199.99 = $199.99  
   - **Total Products Bought:** 1  
   - **Total Cost:** $199.99  

4. **Customer ID: 2** (Second Sale)  
   - **Name:** Jane Smith (continued)  
   - **Products Bought:**  
     - Running Shoes (Product ID: 201)  
       - Quantity: 1  
       - Total Cost: 1 * $79.99 = $79.99  
   - **Total Products Bought:** 1  
   - **Total Cost:** $79.99  

5. **Customer ID: 3** (Second Sale)   
   - **Name:** Emily Johnson (continued)  
   - **Products Bought:**  
     - Running Shoes (Product ID: 201)  
       - Quantity: 1  
       - Total Cost: 1 * $79.99 = $79.99  
   - **Total Products Bought:** 1  
   - **Total Cost:** $79.99  

6. **Customer ID: 3** (Third Sale)  
   - **Name:** Emily Johnson (continued)  
   - **Products Bought:**  
     - Leather Wallet (Product ID: 202)  
       - Quantity: 1  
       - Total Cost: 1 * $39.99 = $39.99  
   - **Total Products Bought:** 1  
   - **Total Cost:** $39.99  

**Summary**  
- **Customer 1 (John Doe):** Total Products = 2, Total Cost = $49.98  
- **Customer 2 (Jane Smith):** Total Products = 2, Total Cost = $79.98 + $79.99 = $159.97  
- **Customer 3 (Emily Johnson):** Total Products = 3 Total Cost = $199.99 + $79.99 + $39.99 = $319.97  

Overall, here are the total purchases for each customer:  
- **John Doe:** 2 Products, $49.98  
- **Jane Smith:** 2 Products, $159.97  
- **Emily Johnson:** 3 Products, $319.97
```
