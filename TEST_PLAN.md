# Test Plan

## Objective
Memastikan seluruh fitur Task Manager berjalan sesuai requirement dan stabil terhadap invalid input.

## Scope
- Add task
- Update task status
- Delete task
- Search task by assignee

## Out of Scope
- UI/frontend testing
- Database integration

## Test Approach
- Black box testing
- Unit testing
- Edge case testing
- Automated testing menggunakan pytest

## Environment
- Python 3.14
- Pytest
- GitHub Actions
- Windows 10

## Test Data
Sample task data dengan kondisi valid dan invalid.

## Entry Criteria
Source code selesai dibuat dan dapat dijalankan.

## Exit Criteria
Seluruh test case berhasil dijalankan tanpa critical defect.

## Deliverables
- Test case
- RTM
- Defect report
- Metrics
- Automated testing result