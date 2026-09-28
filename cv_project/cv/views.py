from django.shortcuts import render


def cv(request):
    context = {
        "name": "Ruixin Xu",
        "email": "18721349662@163.com",
        "phone": "(+1) 484-880-6853",
        "location": "New York, NY",

        "educations": [
            {
                "school": "New York University",
                "degree": "M.S. in Computer Science",
                "year": "2026–present",
                "description": "Graduate studies in Computer Science."
            },
            {
                "school": "Fudan University",
                "degree": "B.S. in Data Science and Big Data Technology",
                "year": "2020–2024",
                "description": "Coursework included Statistics, Optimization, Database Systems, Machine Learning, Image Processing and Visualization, and Stochastic Processes."
            }
        ],
        
        "experiences": [
            {
                "company": "Shanghai HuaRui Bank Co., Ltd.",
                "position": "Data Scientist",
                "year": "2024.07–2025.09",

                "projects": [
                    {
                        "name": "LLM Entity Matching Assistant",
                        "role": "Independent Researcher and Developer",
                        "description": [
                            "Researched natural language understanding capabilities of LLMs in complex business settings.",
                            "Conducted in-depth context engineering for the Qwen2-32B model on Hiagent platform.",
                            "Designed a method combining semantic matching and few-shot prompting, increasing efficiency by over 70%.",
                            "Developed a Python/FastAPI backend using asynchronous programming for concurrent Agent API calls.",
                            "Built an HTML/JavaScript interface supporting document upload and result download."
                        ]
                    },
                    {
                        "name": "Unified Data Reporting Platform (\"Yi Biao Tong\")",
                        "role": "Technical Lead",
                        "description": [
                            "Led data requirement analysis and authored 74 data requirement specifications.",
                            "Created 157 new tables to establish a robust feature repository.",
                            "Developed automated ETL processes using SQL and Python across ODPS and ADB.",
                            "Implemented automated partition management to resolve storage constraints.",
                            "Configured 227 scheduling nodes across 11 workflows to ensure pipeline reliability and automation."
                        ]
                    }
                ]
            }
        ],

        "internships": [
            {
                "company": "Shanghai Qifu Intelligent Technology Co., Ltd.",
                "position": "Intelligent Control System Engineer Intern",
                "year": "2023.09–2024.02",
                "description": [
                    "Assisted in designing an intelligent control system for the hot-dip galvanizing process.",
                    "Integrated Gaussian Process Regression and Gaussian Mixture Model techniques.",
                    "Analyzed relationships between zinc layer thickness, speed, and air knife pressure.",
                    "Used Python and Matplotlib for data analysis and visualization.",
                    "Implemented MongoDB for large-scale process data storage and retrieval.",
                    "Reduced error rates by 20% and Mean Absolute Error by 15% through parameter optimization.",
                    "Reduced material waste by 15% through optimized control parameters."
                ]
            },
            {
                "company": "Shanghai Sito Measurement Technology Co., Ltd.",
                "position": "Measurement Engineer Intern",
                "year": "2023.04–2023.07",
                "description": [
                    "Performed steel plate thickness testing and data processing using Python and MATLAB.",
                    "Used NumPy and Pandas to organize large datasets.",
                    "Developed multi-model fitting approaches for alloy thickness measurement.",
                    "Applied machine learning methods to analyze the nonlinear effects of alloy composition.",
                    "Implemented automated anomaly detection scripts and visualized measurement trends."
                ]
            }
        ],

        "competitions": [
            {
                "name": "Financial Risk Control Modeling Competition",
                "year": "2025.05",
                "description": [
                    "Trained a credit risk model using 264,000 credit data samples.",
                    "Developed a feature selection pipeline using IV, ANOVA, and model importance metrics.",
                    "Selected 500 key variables from 3,029 features.",
                    "Applied LightGBM and Random Forest models.",
                    "Achieved an AUC of 0.91 on an independent validation set."
                ]
            },
            {
                "name": "Mathematical Contest in Modelling (MCM)",
                "year": "2023.02",
                "description": [
                    "Built a model to predict daily Wordle report scores using R.",
                    "Applied time series analysis and Gradient Boosting Decision Trees.",
                    "Used K-means clustering to classify words into difficult, medium, and easy categories."
                ]
            }
        ],

        "projects": [
            {
                "name": "AI Slot Machine Project",
                "year": "2023.09",
                "description": [
                    "Experimented with Q-learning and A2C to optimize reward uncertainty.",
                    "Implemented a multi-armed bandit model to estimate the expected utility of each slot machine arm.",
                    "Optimized model parameters to maximize rewards within a limited number of attempts."
                ]
            },
            {
                "name": "WeChat Mini Program Attendance System",
                "year": "2022.05",
                "description": [
                    "Designed a WeChat Mini Program attendance system.",
                    "Implemented MySQL database support for relationships between users, majors, and departments.",
                    "Designed ER diagrams and optimized the database structure according to third-normal-form principles.",
                    "Implemented Java pages with JDBC database connectivity."
                ]
            }
        ],

        "skills": [
            "Python",
            "SQL",
            "R",
            "SPSS",
            "MATLAB",
        ],

        "languages": [
            "Mandarin — Native",
            "English — Fluent"
        ],

    }

    return render(request, "cv.html", context)