# AI Coding Agent Instructions

## Project Overview
This is an **educational Python project** focused on teaching dictionaries and loops through real-world database challenges. The codebase consists of progressive coding exercises that simulate actual database operations (student lookup, hospital patient management, food delivery orders).

## Architecture & Data Patterns

### Core Data Structure Pattern
All challenges follow a **list of dictionaries** pattern:
```python
# Example from day_1_activities/student_data.py
students = [
    {
        "CPSID": 10000011,
        "Combo,Name": "Anderson, Karen",  # Format: "Last, First"
        "LName": "Anderson",
        "FName": "Karen",
        "MName": "Lynn",
        "HR": "B211",  # Homeroom
        "GL": 10,      # Grade Level
        "Email": ["primary@example.com", "secondary@example.net"]  # Always 2 emails
    },
    # ... more records
]
```

**Key invariants:**
- Each record is a dictionary with consistent keys across all entries
- Email is always a **list with 2 elements** (primary, secondary)
- Name combinations use format `"Last, First"` in `Combo,Name` field
- Unique identifier fields: `CPSID` (students), `PatientID` (hospital), `order_id` (orders)

### Multi-Day Challenge Progression
- **Day 1** (`day_1_activities/`): Dictionary basics, searching, data addition
- **Day 2** (`day_2_challenge/`): Hospital patient system with CRUD operations
- **Day 3** (`day_3_uber_eats_challenge/`): Food delivery order management

Each day's challenge imports external data modules (e.g., `import student_data`).

## Developer Workflows & Patterns

### Data Import Pattern
Challenges import data from separate `_data.py` or module files:
```python
# day_1_activities/2_main.py
import student_data
students = student_data.students
```
Always reference external data through module imports, not hardcoding.

### Typical Challenge Structure
1. **Search functionality**: Find records by name or ID
2. **Data validation**: Prevent duplicate unique IDs
3. **Add new records**: User input → dictionary → append to list
4. **Update/Delete**: Modify or remove records safely
5. **Display results**: Format output for readability

### Common Operations
- **Searching**: Use `for` loops with conditional checks on dictionary keys
- **Duplicate prevention**: Check if unique ID already exists before adding
- **Formatting**: Combine `FName` + `LName` into `"Last, First"` format
- **Nested access**: Email access uses double indexing: `student['Email'][0]` (primary), `student['Email'][1]` (secondary)

## Critical Implementation Notes

### Email Handling
Email is always stored as a list with exactly 2 elements:
- Index `[0]` = primary email
- Index `[1]` = secondary email

When adding new records, always collect both emails and store as `["primary", "secondary"]`.

### Name Formatting
The system uses multiple name fields:
- `LName`: Last name only
- `FName`: First name only
- `MName`: Middle name
- `Combo,Name`: Combined as `"LastName, FirstName"` (this is the display format)

When creating new records, always compute `Combo,Name` from `FName` and `LName`.

### Unique ID Enforcement
Before adding any record, always check for existing ID to prevent duplicates:
```python
# Pattern from challenges
for existing_record in records:
    if existing_record['CPSID'] == new_id:
        print("Duplicate ID - cannot add")
        return
```

## Project-Specific Conventions
- **Variable naming**: Imported data is always pluralized (`students`, `patients`, `orders`)
- **Loop variable naming**: Singular form of data (`for student in students`)
- **User prompts**: Descriptive ("Enter student's full name:", "Enter Patient ID:")
- **Confirmation messages**: Always show total record count after adding new entries
- **Status fields**: Always validate status against expected values (e.g., "Placed", "Preparing", "Out for Delivery")

## Files to Reference
- [day_1_activities/student_data.py](day_1_activities/student_data.py) — Example of complete data structure with 30+ records
- [day_1_activities/3_mini_challenge_day1.py](day_1_activities/3_mini_challenge_day1.py) — Student lookup system requirements
- [day_3_uber_eats_challenge/orders.py](day_3_uber_eats_challenge/orders.py) — Order data with nested lists and status tracking

## What NOT to Do
- Don't use classes or functions beyond basic learner level
- Don't add external dependencies; only use built-in Python (lists, dicts, loops)
- Don't modify data structure formats; keep dictionary keys consistent with examples
- Don't use list comprehensions or advanced patterns (this is educational code)
