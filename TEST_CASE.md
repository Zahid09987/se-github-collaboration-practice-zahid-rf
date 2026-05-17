# Positive Test Case

| TC ID | Scenario | Expected Result |
|---|---|---|
| TC-01 | Add valid task | Task berhasil ditambahkan |
| TC-02 | Update valid status | Status berubah |
| TC-03 | Search valid assignee | Data ditemukan |

# Negative Test Case

| TC ID | Scenario | Expected Result |
|---|---|---|
| TC-04 | Invalid priority | Ditolak |
| TC-05 | Invalid status | Ditolak |
| TC-06 | Whitespace title | Ditolak |

# Edge Test Case

| TC ID | Scenario | Expected Result |
|---|---|---|
| TC-07 | Delete nonexistent task | Sistem stabil |
| TC-08 | Search nonexistent assignee | Return empty list |
| TC-09 | Empty task list | Sistem stabil |