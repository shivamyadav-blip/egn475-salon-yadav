# Nexa Salon - User Stories and Acceptance Criteria

**Student:** Shivam Birat Yadav
**Course:** EGN 475 - Software Prototyping
**University:** Atlantis University
**Project:** Nexa Salon Appointment Booking System
**Assignment:** Week 2 - Assignment 2.1

## Project Overview

Nexa Salon is a salon appointment booking prototype designed to make scheduling easier for clients and staff. Clients can explore services, check available times, and book appointments without waiting for staff to respond. Staff can view appointments and update their status.

## Personas

- **Client:** A person who wants to book and manage salon appointments quickly.
- **Salon Staff:** An employee who manages the salon's appointment schedule.

## User Stories

### US-01: View Salon Services
**Priority:** Must Have

As a salon client, I want to view available salon services so that I can choose the treatment that fits my needs.

**Acceptance Criteria:**
1. Given the salon has services listed, when I open the services page, then I can see the name, description, and price of each service.
2. Given the salon has no services available, when I open the services page, then I see a message saying no services are currently available.

### US-02: View Available Appointment Times
**Priority:** Must Have

As a salon client, I want to view available appointment times for a selected service and date so that I can choose a convenient time.

**Acceptance Criteria:**
1. Given I have selected a service and date with open slots, when I view available times, then only unbooked slots for that service and date appear.
2. Given a time slot is already booked, when I view available times for that date, then the booked slot is not offered.

### US-03: Book an Appointment
**Priority:** Must Have

As a salon client, I want to book an appointment using my contact details and a selected time so that I can reserve a salon visit.

**Acceptance Criteria:**
1. Given I have entered my name, contact information, service, and an available time, when I submit my booking, then the appointment is saved and the selected slot becomes unavailable.
2. Given I leave a required field empty, when I submit my booking, then I see a clear validation message and no appointment is created.

### US-04: View Booking Confirmation
**Priority:** Must Have

As a salon client, I want to see a booking confirmation so that I know my appointment was successfully reserved.

**Acceptance Criteria:**
1. Given my appointment was saved successfully, when the booking completes, then I see a confirmation with the service, date, time, and booking reference.
2. Given the appointment could not be saved, when the booking fails, then I see an error message instead of a success confirmation.

### US-05: View Staff Appointment Schedule
**Priority:** Must Have

As a salon staff member, I want to view scheduled appointments for a selected day so that I can prepare for upcoming clients.

**Acceptance Criteria:**
1. Given I am an authorized staff member and appointments exist for the selected day, when I open the schedule, then I see those appointments with their times, services, and statuses.
2. Given I am not authorized as salon staff, when I try to open the staff schedule, then access is denied.

### US-06: Update Appointment Status
**Priority:** Must Have

As a salon staff member, I want to update an appointment's status so that the schedule reflects its current progress.

**Acceptance Criteria:**
1. Given I am authorized staff and an appointment is booked, when I change its status to Completed, then the new status is saved and displayed.
2. Given an appointment is already canceled, when I try to mark it Completed, then the change is rejected and the status stays Canceled.

### US-07: Cancel an Appointment
**Priority:** Should Have

As a salon client, I want to cancel my appointment using my booking reference and contact information so that I can release a time I no longer need.

**Acceptance Criteria:**
1. Given I provide matching booking details for a future appointment, when I confirm cancellation, then the appointment is marked Canceled and its time becomes available again.
2. Given my booking reference or contact information does not match, when I request cancellation, then no appointment is changed and I see an error message.

### US-08: View Daily Appointment Total
**Priority:** Could Have

As a salon staff member, I want to see the total number of appointments scheduled for a day so that I can understand the salon's workload.

**Acceptance Criteria:**
1. Given I am authorized staff and appointments exist for a selected day, when I view the daily summary, then I see the number of appointments that are not canceled.
2. Given there are no active appointments for the selected day, when I view the daily summary, then the total displays zero.

## Prioritization Summary

- Must Have: US-01, US-02, US-03, US-04, US-05, US-06
- Should Have: US-07
- Could Have: US-08

The six must-have stories define the main prototype. The should-have and could-have stories can be developed after the essential booking and staff features are working.

## INVEST Review Preparation

The stories are written to be independent where practical, negotiable, valuable to users, estimable, small enough for a prototype, and testable. Each story has two Given/When/Then acceptance criteria, including an error or edge case.

Copilot review findings and final decisions will be recorded in the assignment PDF after the actual review is completed.
