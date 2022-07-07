# EPIC: Chicken Coop 2.0

---

A RESTful app for helping farmers manage chicken coops easier.
The owner is able to manage chickens and to access useful stats and projections.

### Usecase:
At the end of each day, the farm manager introduces manually informations 
into the system

---
**Stack: python, flask, sqlite**

---
### The tasks for today:

[DEV-01] Create a REST endpoint
- this REST endpoint will be used for handling `chicken` resource
- TBD `chicken` resource attributes

[DEV-02] Create a `/report` page
- We want to display for the each day in the current week:
  - number of chickens
  - egg count
  - chicks count
  - how many died
- TBD can we improve this?

[DEV-03] Support real-time egg counting
- We want to support real time inputs from devices counting eggs and monitoring chicken health
