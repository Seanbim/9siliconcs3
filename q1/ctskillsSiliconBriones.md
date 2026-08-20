# Computational Thinking Exercise
## Smart School Canteen Queue
**Section:** 9-Silicon
**Last Name:** Briones
**Date:** August 20, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The school canteen needs an efficient queue system to manage students during busy periods because a large number of students may need to order and receive their food within a limited amount of time.
---
## Step 2: Identify the Sub-Problems
1. Students need to join and maintain an organized queue.
2. The system needs to determine which student should be served next.
3. The system needs to process each student's order efficiently.
4. The system needs to remove students from the queue after they have received their orders.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Difficulty joining the queue | Decomposition | Break the queuing process into smaller steps. |
| Difficulty identifying the next student | Pattern Recognition | Follow the first-in, first-out pattern. |
| Slow order processing | Abstraction | Focus only on essential order details. |
| Students remaining in the queue after being served | Algorithm Design | Create steps to serve and remove each student. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
This is for all of them all at once.
### Pseudocode
START

Check if the queue contains any students.

IF the queue is empty THEN
    Display "No students are waiting."
ELSE
    Identify the student at the front of the queue.
    Display the student's position in the queue.
    Call the student to the counter.
    
    Ask for the student's order.
    Record the order.
    Calculate the total cost.
    
    Ask the student for payment.
    
    IF payment is enough THEN
        Calculate the change.
        Give the order to the student.
        Give the change to the student.
        Remove the student from the front of the queue.
        Display "Transaction complete."
    ELSE
        Display "Insufficient payment."
        Ask for the correct payment.
    END IF
END IF

Check if more students are waiting.

IF more students are waiting THEN
    Identify the next student at the front of the queue.
ELSE
    Display "Queue is empty."
END IF


END
---