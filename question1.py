book1 = int(input("Enter Total Number of books for Introduction to python programming: "))
book2 = int(input("Enter Total Number of books for  Python Libraries Cookbook:  "))
book3 = int(input("Enter Total Number of books for Data Science in Python: "))
cost_Book1= 499.00
cost_Book2 = 855.00
cost_Book3 = 645.00
GST = 12/100
delivary_charges = 250.00
Total_Price= (book1*cost_Book1) + (book2*cost_Book2) + (book3*cost_Book3) + delivary_charges
Gst_Amount = Total_Price * GST 
Total_InvoiceAmount = Total_Price + Gst_Amount
print("The total invoice amount is : ",Total_InvoiceAmount) 