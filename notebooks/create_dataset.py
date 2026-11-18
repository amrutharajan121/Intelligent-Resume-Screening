import pandas as pd


data = [

    # --------------------------------------------------
    # SOFTWARE DEVELOPER
    # --------------------------------------------------

    ["Software developer skilled in Java Python C++ SQL Git object oriented programming software development", "Software Developer"],
    ["Software engineer experienced in Java Spring Boot SQL REST API Git and backend development", "Software Developer"],
    ["Software developer with experience in Python Django Java databases APIs and application development", "Software Developer"],
    ["Backend developer skilled in Java Node.js Express MongoDB REST APIs and Git", "Software Developer"],
    ["Software engineer experienced in C# .NET SQL Git API development and software engineering", "Software Developer"],
    ["Developer with strong programming skills in Java Python SQL data structures algorithms and Git", "Software Developer"],
    ["Software developer experienced in Java application development SQL databases and Git", "Software Developer"],
    ["Backend software engineer skilled in Java Spring Boot REST APIs PostgreSQL and Docker", "Software Developer"],
    ["Application developer experienced in Python Java SQL APIs and software testing", "Software Developer"],
    ["Software engineer skilled in object oriented programming Java databases APIs and version control", "Software Developer"],


    # --------------------------------------------------
    # WEB DEVELOPER
    # --------------------------------------------------

    ["Web developer skilled in HTML CSS JavaScript React responsive web design and frontend development", "Web Developer"],
    ["Frontend developer experienced in HTML CSS JavaScript React and modern web applications", "Web Developer"],
    ["Web developer with experience in JavaScript Node.js Express MongoDB HTML CSS", "Web Developer"],
    ["Full stack web developer skilled in React Node.js Express SQL HTML CSS JavaScript", "Web Developer"],
    ["Web developer experienced in Next.js React JavaScript Tailwind CSS and responsive websites", "Web Developer"],
    ["Frontend engineer skilled in HTML CSS JavaScript React UI development and web technologies", "Web Developer"],
    ["Web developer skilled in Bootstrap HTML CSS JavaScript and responsive design", "Web Developer"],
    ["Frontend developer experienced in React JavaScript CSS HTML and user interface development", "Web Developer"],
    ["Full stack developer skilled in React Node.js Express MongoDB HTML CSS", "Web Developer"],
    ["Web application developer experienced in JavaScript React REST APIs and responsive design", "Web Developer"],


    # --------------------------------------------------
    # MACHINE LEARNING ENGINEER
    # --------------------------------------------------

    ["Machine learning engineer skilled in Python TensorFlow Keras PyTorch scikit-learn machine learning models", "Machine Learning Engineer"],
    ["ML engineer experienced in deep learning neural networks NLP Python TensorFlow and model deployment", "Machine Learning Engineer"],
    ["Machine learning professional skilled in Python scikit-learn TensorFlow pandas numpy and machine learning", "Machine Learning Engineer"],
    ["AI engineer experienced in machine learning deep learning NLP neural networks and Python", "Machine Learning Engineer"],
    ["Machine learning engineer with experience in model training feature engineering Python TensorFlow and PyTorch", "Machine Learning Engineer"],
    ["ML developer skilled in artificial intelligence machine learning algorithms deep learning and Python", "Machine Learning Engineer"],
    ["Machine learning engineer experienced in classification regression Python and scikit-learn", "Machine Learning Engineer"],
    ["AI engineer skilled in TensorFlow neural networks computer vision and Python", "Machine Learning Engineer"],
    ["Machine learning professional experienced in NLP model development feature engineering and Python", "Machine Learning Engineer"],
    ["ML engineer skilled in predictive modeling deep learning TensorFlow PyTorch and Python", "Machine Learning Engineer"],


    # --------------------------------------------------
    # DATA SCIENTIST
    # --------------------------------------------------

    ["Data scientist skilled in Python pandas numpy machine learning statistics data visualization and SQL", "Data Scientist"],
    ["Data science professional experienced in statistical analysis machine learning Python pandas and scikit-learn", "Data Scientist"],
    ["Data scientist with experience in predictive modeling data analysis Python SQL and machine learning", "Data Scientist"],
    ["Data science professional skilled in Python statistics pandas numpy matplotlib and machine learning", "Data Scientist"],
    ["Data scientist experienced in exploratory data analysis feature engineering predictive analytics and Python", "Data Scientist"],
    ["Data science engineer skilled in machine learning statistics SQL Python and data visualization", "Data Scientist"],
    ["Data scientist skilled in Python machine learning statistics SQL and predictive analytics", "Data Scientist"],
    ["Data science professional experienced in pandas numpy visualization and statistical modeling", "Data Scientist"],
    ["Data scientist experienced in data preprocessing feature engineering machine learning and Python", "Data Scientist"],
    ["Data scientist skilled in SQL Python statistics data visualization and predictive modeling", "Data Scientist"],


    # --------------------------------------------------
    # DATA ANALYST
    # --------------------------------------------------

    ["Data analyst skilled in SQL Excel Python pandas data visualization and business analysis", "Data Analyst"],
    ["Data analyst experienced in Excel SQL Power BI data cleaning reporting and dashboards", "Data Analyst"],
    ["Data analyst skilled in SQL Excel Python Tableau data visualization and reporting", "Data Analyst"],
    ["Business data analyst experienced in data analysis Excel SQL dashboards and business reports", "Data Analyst"],
    ["Data analyst with strong skills in Excel SQL Power BI statistics and data interpretation", "Data Analyst"],
    ["Data analytics professional experienced in reporting dashboards SQL Excel and data visualization", "Data Analyst"],
    ["Data analyst skilled in Excel SQL Power BI reporting and data cleaning", "Data Analyst"],
    ["Data analyst experienced in SQL dashboards Excel business reports and visualization", "Data Analyst"],
    ["Data professional skilled in Excel SQL Tableau data analysis and reporting", "Data Analyst"],
    ["Data analyst experienced in business intelligence SQL Excel and dashboard development", "Data Analyst"],


    # --------------------------------------------------
    # ACCOUNTANT
    # --------------------------------------------------

    ["Accountant experienced in bookkeeping financial statements journal entries ledger accounts taxation and Excel", "Accountant"],
    ["Accounting professional skilled in accounts payable accounts receivable bookkeeping GST and financial reporting", "Accountant"],
    ["Accountant with experience in Tally Excel balance sheets income statements auditing and taxation", "Accountant"],
    ["Finance and accounting professional skilled in bookkeeping payroll taxation invoices and financial records", "Accountant"],
    ["Accountant experienced in general ledger reconciliation GST TDS financial statements and Excel", "Accountant"],
    ["Accounting executive skilled in Tally ERP bookkeeping invoices accounts payable and accounts receivable", "Accountant"],
    ["Accountant skilled in bookkeeping journal entries ledger reconciliation and financial reporting", "Accountant"],
    ["Accounting professional experienced in GST TDS payroll and financial statements", "Accountant"],
    ["Accountant experienced in Tally ERP Excel auditing taxation and accounts management", "Accountant"],
    ["Accounting executive skilled in accounts payable receivable bookkeeping and invoicing", "Accountant"],


    # --------------------------------------------------
    # FINANCIAL ANALYST
    # --------------------------------------------------

    ["Financial analyst skilled in financial modeling forecasting budgeting investment analysis and Excel", "Financial Analyst"],
    ["Finance analyst experienced in financial statements valuation forecasting and business analysis", "Financial Analyst"],
    ["Financial analyst skilled in Excel financial modeling data analysis budgeting and forecasting", "Financial Analyst"],
    ["Finance professional experienced in investment analysis financial reporting valuation and risk analysis", "Financial Analyst"],
    ["Financial analyst with skills in corporate finance financial modeling forecasting and Excel", "Financial Analyst"],
    ["Finance analyst experienced in profitability analysis budgeting forecasting and financial planning", "Financial Analyst"],
    ["Financial analyst skilled in investment research valuation financial modeling and Excel", "Financial Analyst"],
    ["Finance professional experienced in forecasting budgeting financial analysis and reporting", "Financial Analyst"],
    ["Financial analyst experienced in corporate finance financial planning and business analysis", "Financial Analyst"],
    ["Finance analyst skilled in financial statements forecasting valuation and investment analysis", "Financial Analyst"],


    # --------------------------------------------------
    # HR EXECUTIVE
    # --------------------------------------------------

    ["HR executive experienced in recruitment employee relations payroll onboarding and human resources", "HR Executive"],
    ["Human resources professional skilled in recruitment interviews employee engagement and HR operations", "HR Executive"],
    ["HR executive experienced in talent acquisition employee records onboarding and performance management", "HR Executive"],
    ["Human resource executive skilled in recruitment screening payroll employee engagement and HR policies", "HR Executive"],
    ["HR professional experienced in hiring recruitment employee relations training and onboarding", "HR Executive"],
    ["HR executive skilled in talent management recruitment employee engagement and organizational development", "HR Executive"],
    ["HR professional experienced in recruitment employee onboarding payroll and HR administration", "HR Executive"],
    ["Human resources executive skilled in recruitment interviews employee relations and HR operations", "HR Executive"],
    ["HR executive experienced in employee engagement performance management and recruitment", "HR Executive"],
    ["HR specialist skilled in talent acquisition onboarding training and employee management", "HR Executive"],


    # --------------------------------------------------
    # MARKETING EXECUTIVE
    # --------------------------------------------------

    ["Marketing executive experienced in digital marketing social media marketing SEO content marketing and campaigns", "Marketing Executive"],
    ["Marketing professional skilled in brand management social media SEO Google Ads and marketing campaigns", "Marketing Executive"],
    ["Digital marketing executive experienced in SEO SEM social media content creation and analytics", "Marketing Executive"],
    ["Marketing executive skilled in market research advertising campaign management and digital marketing", "Marketing Executive"],
    ["Marketing professional experienced in social media marketing email marketing SEO and brand promotion", "Marketing Executive"],
    ["Marketing executive with experience in digital campaigns market research customer engagement and branding", "Marketing Executive"],
    ["Marketing professional skilled in content marketing social media SEO and advertising campaigns", "Marketing Executive"],
    ["Digital marketing executive experienced in Google Ads SEO social media and campaign analytics", "Marketing Executive"],
    ["Marketing executive skilled in brand promotion market research customer engagement and digital marketing", "Marketing Executive"],
    ["Marketing professional experienced in email campaigns social media marketing SEO and branding", "Marketing Executive"],


    # --------------------------------------------------
    # SALES EXECUTIVE
    # --------------------------------------------------

    ["Sales executive experienced in lead generation customer acquisition sales targets negotiation and CRM", "Sales Executive"],
    ["Sales professional skilled in client relationship management lead conversion business development and negotiation", "Sales Executive"],
    ["Sales executive experienced in cold calling lead generation customer relationships and achieving sales targets", "Sales Executive"],
    ["Business development executive skilled in sales negotiation customer acquisition and CRM systems", "Sales Executive"],
    ["Sales professional experienced in account management lead generation client communication and sales strategy", "Sales Executive"],
    ["Sales executive skilled in B2B sales customer relationship management prospecting and business development", "Sales Executive"],
    ["Sales executive experienced in lead generation client communication negotiation and sales targets", "Sales Executive"],
    ["Sales professional skilled in customer acquisition account management and business development", "Sales Executive"],
    ["Business development professional experienced in sales prospecting CRM and client relationships", "Sales Executive"],
    ["Sales executive skilled in B2B sales lead conversion customer management and negotiation", "Sales Executive"],


    # --------------------------------------------------
    # BUSINESS ANALYST
    # --------------------------------------------------

    ["Business analyst skilled in requirements gathering business process analysis SQL documentation and stakeholder management", "Business Analyst"],
    ["Business analyst experienced in requirement analysis process improvement data analysis and stakeholder communication", "Business Analyst"],
    ["Business analyst skilled in business requirements functional requirements SQL and project documentation", "Business Analyst"],
    ["Business analysis professional experienced in process mapping stakeholder management requirement gathering and reporting", "Business Analyst"],
    ["Business analyst experienced in Agile requirements analysis user stories documentation and business intelligence", "Business Analyst"],
    ["Business analyst skilled in data analysis process improvement stakeholder communication and requirements management", "Business Analyst"],
    ["Business analyst experienced in requirement gathering business process modeling and stakeholder management", "Business Analyst"],
    ["Business analysis professional skilled in SQL documentation process improvement and requirements analysis", "Business Analyst"],
    ["Business analyst experienced in Agile user stories functional requirements and stakeholder communication", "Business Analyst"],
    ["Business analyst skilled in process analysis reporting requirements gathering and business intelligence", "Business Analyst"],


    # --------------------------------------------------
    # MECHANICAL ENGINEER
    # --------------------------------------------------

    ["Mechanical engineer skilled in CAD AutoCAD SolidWorks machine design manufacturing and mechanical systems", "Mechanical Engineer"],
    ["Mechanical engineering graduate experienced in AutoCAD SolidWorks production engineering and mechanical design", "Mechanical Engineer"],
    ["Mechanical engineer skilled in thermodynamics manufacturing engineering CAD and machine design", "Mechanical Engineer"],
    ["Mechanical engineer experienced in production maintenance quality control and mechanical equipment", "Mechanical Engineer"],
    ["Mechanical engineering professional skilled in SolidWorks AutoCAD product design manufacturing and CNC", "Mechanical Engineer"],
    ["Mechanical engineer experienced in mechanical design engineering manufacturing processes and maintenance", "Mechanical Engineer"],
    ["Mechanical engineer skilled in CAD machine design manufacturing and production engineering", "Mechanical Engineer"],
    ["Mechanical engineering professional experienced in SolidWorks AutoCAD CNC and product design", "Mechanical Engineer"],
    ["Mechanical engineer skilled in thermodynamics manufacturing maintenance and mechanical systems", "Mechanical Engineer"],
    ["Mechanical engineer experienced in production engineering CAD design and industrial equipment", "Mechanical Engineer"],


    # --------------------------------------------------
    # CIVIL ENGINEER
    # --------------------------------------------------

    ["Civil engineer skilled in AutoCAD structural design construction project management and site supervision", "Civil Engineer"],
    ["Civil engineering professional experienced in construction site management quantity surveying and AutoCAD", "Civil Engineer"],
    ["Civil engineer skilled in structural engineering construction planning estimation and project supervision", "Civil Engineer"],
    ["Civil engineer experienced in building construction road projects AutoCAD and site management", "Civil Engineer"],
    ["Civil engineering professional skilled in surveying structural design construction materials and project management", "Civil Engineer"],
    ["Civil engineer experienced in construction planning quantity estimation site supervision and structural engineering", "Civil Engineer"],
    ["Civil engineer skilled in AutoCAD construction planning structural design and surveying", "Civil Engineer"],
    ["Civil engineering professional experienced in site supervision quantity surveying and project management", "Civil Engineer"],
    ["Civil engineer skilled in construction estimation structural engineering and AutoCAD", "Civil Engineer"],
    ["Civil engineer experienced in building projects road construction site management and surveying", "Civil Engineer"],


    # --------------------------------------------------
    # ELECTRICAL ENGINEER
    # --------------------------------------------------

    ["Electrical engineer skilled in circuit design electrical systems power systems PLC and electrical maintenance", "Electrical Engineer"],
    ["Electrical engineering professional experienced in electrical circuits power distribution control systems and maintenance", "Electrical Engineer"],
    ["Electrical engineer skilled in AutoCAD electrical PLC SCADA motors and industrial automation", "Electrical Engineer"],
    ["Electrical engineer experienced in power systems electrical equipment wiring and industrial maintenance", "Electrical Engineer"],
    ["Electrical engineering professional skilled in circuit analysis control systems instrumentation and power electronics", "Electrical Engineer"],
    ["Electrical engineer experienced in electrical design testing troubleshooting maintenance and automation", "Electrical Engineer"],
    ["Electrical engineer skilled in circuit design PLC automation power systems and maintenance", "Electrical Engineer"],
    ["Electrical engineering professional experienced in power distribution electrical testing and control systems", "Electrical Engineer"],
    ["Electrical engineer skilled in SCADA PLC industrial automation and electrical systems", "Electrical Engineer"],
    ["Electrical engineer experienced in electrical equipment maintenance circuit analysis and troubleshooting", "Electrical Engineer"],


    # --------------------------------------------------
    # TEACHER
    # --------------------------------------------------

    ["Teacher experienced in classroom management lesson planning student assessment curriculum development and teaching", "Teacher"],
    ["School teacher skilled in lesson planning classroom instruction student evaluation and educational activities", "Teacher"],
    ["Teacher experienced in curriculum planning classroom management student engagement and academic assessment", "Teacher"],
    ["Educator skilled in teaching lesson preparation student mentoring classroom activities and assessment", "Teacher"],
    ["Teacher experienced in developing learning materials student guidance examinations and classroom instruction", "Teacher"],
    ["Education professional skilled in teaching curriculum development student counseling and academic planning", "Teacher"],
    ["Teacher experienced in classroom instruction lesson planning student evaluation and mentoring", "Teacher"],
    ["Educator skilled in curriculum development student engagement assessment and classroom management", "Teacher"],
    ["Teacher experienced in academic planning learning materials examinations and student guidance", "Teacher"],
    ["School educator skilled in teaching classroom management student assessment and curriculum planning", "Teacher"],


    # --------------------------------------------------
    # HEALTHCARE ADMINISTRATOR
    # --------------------------------------------------

    ["Healthcare administrator experienced in hospital administration patient records healthcare operations and scheduling", "Healthcare Administrator"],
    ["Healthcare management professional skilled in hospital operations patient coordination medical records and administration", "Healthcare Administrator"],
    ["Healthcare administrator experienced in hospital management patient services staff coordination and healthcare operations", "Healthcare Administrator"],
    ["Hospital administrator skilled in healthcare management patient registration medical records and operational planning", "Healthcare Administrator"],
    ["Healthcare professional experienced in hospital administration appointment scheduling patient coordination and billing", "Healthcare Administrator"],
    ["Healthcare administrator skilled in medical administration hospital operations patient services and reporting", "Healthcare Administrator"],
    ["Hospital administrator experienced in patient coordination healthcare operations staff management and scheduling", "Healthcare Administrator"],
    ["Healthcare administrator skilled in medical records patient services hospital operations and reporting", "Healthcare Administrator"],
    ["Healthcare management professional experienced in hospital administration patient registration and billing", "Healthcare Administrator"],
    ["Healthcare administrator skilled in hospital operations appointment scheduling patient coordination and administration", "Healthcare Administrator"],


    # --------------------------------------------------
    # QUALITY ANALYST
    # --------------------------------------------------

    ["Quality analyst experienced in software testing test cases defect tracking quality assurance and regression testing", "Quality Analyst"],
    ["Quality analyst skilled in manual testing test automation bug reporting test plans and quality assurance", "Quality Analyst"],
    ["QA analyst experienced in software testing Selenium test cases defect management and regression testing", "Quality Analyst"],
    ["Quality assurance professional skilled in testing documentation bug tracking functional testing and QA processes", "Quality Analyst"],
    ["Quality analyst experienced in test execution defect reporting quality control and software validation", "Quality Analyst"],
    ["QA professional skilled in manual testing automation testing test cases and defect tracking", "Quality Analyst"],
    ["Quality analyst skilled in functional testing regression testing test cases and bug tracking", "Quality Analyst"],
    ["QA analyst experienced in Selenium automation testing defect reporting and test execution", "Quality Analyst"],
    ["Quality assurance analyst skilled in software testing test plans defect management and validation", "Quality Analyst"],
    ["Quality analyst experienced in manual testing quality control regression testing and defect tracking", "Quality Analyst"],


    # --------------------------------------------------
    # DIGITAL ASSOCIATE
    # --------------------------------------------------

    ["Digital associate experienced in data annotation data labeling image annotation audio annotation and quality checking", "Digital Associate"],
    ["Digital associate skilled in content review data processing quality assurance and following standard operating procedures", "Digital Associate"],
    ["Digital operations associate experienced in data labeling annotation content classification and quality checks", "Digital Associate"],
    ["Digital associate skilled in image labeling audio transcription data validation and process compliance", "Digital Associate"],
    ["Digital associate experienced in reviewing digital content data annotation quality control and productivity tracking", "Digital Associate"],
    ["Digital operations professional skilled in data processing content moderation annotation and quality assurance", "Digital Associate"],
    ["Digital associate experienced in image annotation audio labeling data validation and quality checking", "Digital Associate"],
    ["Digital operations associate skilled in content review data processing SOP compliance and quality control", "Digital Associate"],
    ["Digital associate experienced in data labeling content classification productivity tracking and quality assurance", "Digital Associate"],
    ["Digital associate skilled in digital content review annotation data processing and validation", "Digital Associate"],


    # --------------------------------------------------
    # CRM EXECUTIVE
    # --------------------------------------------------

    ["CRM executive experienced in customer relationship management Salesforce CRM lead management and customer support", "CRM Executive"],
    ["CRM professional skilled in Salesforce customer data management lead tracking and client relationships", "CRM Executive"],
    ["CRM executive experienced in customer retention CRM software Salesforce lead management and customer communication", "CRM Executive"],
    ["Customer relationship executive skilled in CRM systems customer support sales tracking and client management", "CRM Executive"],
    ["CRM specialist experienced in Salesforce customer records lead management reporting and customer engagement", "CRM Executive"],
    ["CRM executive skilled in customer relationship management CRM analytics sales pipeline and client communication", "CRM Executive"],
    ["CRM professional experienced in Salesforce customer management lead tracking and customer retention", "CRM Executive"],
    ["CRM executive skilled in customer support Salesforce CRM data management and sales pipeline tracking", "CRM Executive"],
    ["Customer relationship specialist experienced in CRM software client communication lead management and reporting", "CRM Executive"],
    ["CRM executive experienced in Salesforce customer records sales tracking client relationships and CRM analytics", "CRM Executive"]
]


# --------------------------------------------------
# CREATE DATAFRAME
# --------------------------------------------------

df = pd.DataFrame(
    data,
    columns=["resume", "role"]
)


# --------------------------------------------------
# SAVE CLEAN DATASET
# --------------------------------------------------

df.to_csv(
    "notebooks/resume_dataset.csv",
    index=False
)


# --------------------------------------------------
# DISPLAY INFORMATION
# --------------------------------------------------

print("======================================")
print("DATASET CREATED SUCCESSFULLY")
print("======================================")

print("\nTotal resumes:", len(df))

print("\nNumber of roles:", df["role"].nunique())

print("\nResumes per role:")
print(df["role"].value_counts())

print("\nRoles:")

for role in df["role"].unique():
    print("-", role)

print("\nSaved to:")
print("notebooks/resume_dataset.csv")