# Max Profit Problem

## 📌 Problem Overview

Mr. X owns an infinite strip of land in **Mars Land**. He can develop the land by constructing different types of properties. However, **only one property can be constructed at a time** (no parallel construction).

The objective is to **maximize total earnings after `n` units of time** by choosing the optimal mix of properties.

---

## 🏗️ Property Details

| Property Type       | Build Time (units) | Land Size | Earnings per Unit Time |
| ------------------- | ------------------ | --------- | ---------------------- |
| Theatre (T)         | 5                  | 2 × 1     | $1500                  |
| Pub (P)             | 4                  | 1 × 1     | $1000                  |
| Commercial Park (C) | 10                 | 3 × 1     | $2000                  |

---

## ⚙️ Rules & Constraints

* Only **one property** can be developed at any time.
* Earnings start **only after construction is completed**.
* Land size is **not a limiting factor** (infinite land available).
* The goal is to **maximize total earnings** within the given time.

---

## 🎯 Objective

Given a total available time `n`:

* Determine the **optimal combination** of Theatres, Pubs, and Commercial Parks
* Maximize total earnings
* Display the output in the format:

```
T:<number> P:<number> C:<number>
```

---

## 🧪 Test Cases

### ✅ Test Case 1

**Input:**

```
Time Unit: 7
```

**Output:**

```
Earnings: $3000
T:1 P:0 C:0
```

---

### ✅ Test Case 2

**Input:**

```
Time Unit: 8
```

**Output:**

```
Earnings: $4500
T:1 P:0 C:0
```

---

### ✅ Test Case 3

**Input:**

```
Time Unit: 13
```

**Output:**

```
Earnings: $16500
T:2 P:0 C:0
```

---

## 🧠 Solution Approach

1. Iterate through all **valid combinations** of properties that fit within the given time.
2. Calculate total earnings for each valid combination.
3. Track the combination that produces the **maximum profit**.
4. Display the final earnings and property counts.

This approach ensures the optimal solution is always selected.

---

## 📂 Project Structure

```
├── max_profit.py          # Python implementation
├── README.md              # Problem description and explanation
├── screenshot-max-profit.png  # Sample output screenshot
```

---

## ▶️ How to Run

Make sure Python is installed on your system.

```bash
python max_profit.py
```

---

## 👩‍💻 Author

**Vani Priya G**

---

⭐ If you found this project helpful, feel free to give it a star on GitHub!
