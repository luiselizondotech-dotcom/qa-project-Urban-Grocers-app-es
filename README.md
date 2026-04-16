# Urban Grocers — API Integration Testing

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) ![Tests](https://img.shields.io/badge/Endpoints-100%25_Coverage-brightgreen?style=flat-square)

API integration testing project for the **Urban Grocers** grocery delivery application. Covers endpoint validation, JSON schema verification, and response code testing.

## 🎯 What This Project Demonstrates

- **API endpoint testing** using Postman and Python
- **JSON schema validation** for all response structures
- **HTTP status code** verification (200, 201, 400, 404, etc.)
- Full coverage of the Urban Grocers API
- Organized test collection with clear naming conventions

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Test automation scripts |
| Postman | API exploration and manual testing |
| JavaScript | Postman test scripts |
| pytest | Automated test execution |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/luiselizondotech-dotcom/qa-project-Urban-Grocers-app-es

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
```

## 📋 API Coverage

| Endpoint | Method | Tests |
|----------|--------|-------|
| /api/v1/kits | GET, POST | Kits listing and creation |
| /api/v1/products | GET | Products catalog |
| /order/v1 | POST | Order creation |
| /api/v1/couriers | GET | Courier validation |
| Auth endpoints | POST | Token generation |

## 📊 Results

- ✅ 100% endpoint coverage for Urban Grocers API
- ✅ JSON schema validation for all responses
- ✅ HTTP status code verification
- ✅ Positive and negative test scenarios

## 👤 Author

**Luis Elizondo** — QA Engineer
- GitHub: [@luiselizondotech-dotcom](https://github.com/luiselizondotech-dotcom)
- LinkedIn: [qa-engineer-elizondo-luis](https://www.linkedin.com/in/qa-engineer-elizondo-luis)
- Portfolio: [luis-qa-journey.lovable.app](https://luis-qa-journey.lovable.app)
