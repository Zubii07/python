def find_loyal_customers(day1_log, day2_log):
    """
    Find loyal customers who visited on both days and viewed at least 2 unique pages.
    
    Args:
        day1_log: List of dictionaries with keys 'timestamp', 'pageId', 'customerId'
        day2_log: List of dictionaries with keys 'timestamp', 'pageId', 'customerId'
    
    Returns:
        List of customer IDs as strings
    """
    # Get customers and their pages for each day
    day1_customers = {}
    for entry in day1_log:
        customer_id = entry['customerId']
        page_id = entry['pageId']
        if customer_id not in day1_customers:
            day1_customers[customer_id] = set()
        day1_customers[customer_id].add(page_id)
    
    day2_customers = {}
    for entry in day2_log:
        customer_id = entry['customerId']
        page_id = entry['pageId']
        if customer_id not in day2_customers:
            day2_customers[customer_id] = set()
        day2_customers[customer_id].add(page_id)
    
    # Find customers who visited both days
    common_customers = set(day1_customers.keys()) & set(day2_customers.keys())
    
    # Filter customers 
    loyal_customers = []
    for customer_id in common_customers:
        unique_pages = day1_customers[customer_id] | day2_customers[customer_id]
        if len(unique_pages) >= 2:
            loyal_customers.append(customer_id)
    
    return loyal_customers


# Example usage
if __name__ == "__main__":
    day1 = [
        {"timestamp": "1730314108", "pageId": "4", "customerId": "7220"},
        {"timestamp": "1730314108", "pageId": "12", "customerId": "6707"},
        {"timestamp": "1730314108", "pageId": "4", "customerId": "4014"},
        {"timestamp": "1730314108", "pageId": "9", "customerId": "4014"}
    ]
    
    day2 = [
        {"timestamp": "2630314108", "pageId": "4", "customerId": "7220"},
        {"timestamp": "2630314108", "pageId": "4", "customerId": "6707"},
        {"timestamp": "2630314108", "pageId": "4", "customerId": "4014"}
    ]
    
    result = find_loyal_customers(day1, day2)
    print(f"Loyal customers: {result}")
