
## Proposal Details

### Overview

**Tech stack:** Python (Django) + Supabase

**Target users:**
- Individual student learners who use the system for self-paced learning and independent study
- Students with ADHD or attention difficulties who need personalized, customizable reading environments
- Students who struggle to maintain focus while reading course materials or textbooks on their own time

**Description:**

Lessonfy is a web-based personalized study reader and lesson management application designed to help students read, understand, and retain course material by customizing how content is presented and how learning is tracked. The system allows students to create or import lessons in two modes: manual mode where they structure lessons with custom titles and sections, or automatic mode where they upload text files and the system automatically splits content into readable sections. While reading, students can highlight and pin confusing or important passages to named collections with custom color-coding, creating an organized system for tracking difficult concepts. The app provides adjustable reading settings including bionic reading (which highlights the first part of each word for faster scanning), adjustable font size and line spacing, focus mode that reduces distractions, background sound options, and theme preferences, all settings persist across sessions. Every pin is stored and tied to the student's account, allowing Anchor to generate learning reports showing which concepts students struggle with most frequently across lessons. This combination of personalized reading tools and data-driven learning insights helps students identify weak areas, review problem concepts more effectively, and develop better study habits over time.

### Problem & Objectives

**Problem:**

Many students struggle to maintain focus while reading course materials, especially those with ADHD or attention difficulties. Current reading tools assume a one-size-fits-all approach (fixed font, fixed layout, no reading aids), forcing students to adapt to the material instead of the reverse. When students encounter confusing content, they have no systematic way to mark it, revisit it, or track patterns in what they struggle with. This lack of structure and personalization leads to inefficient studying, repeated confusion, and wasted time. Students spend hours reading but retain little because they cannot easily identify which concepts they find difficult, and existing tools provide no feedback on their learning patterns. Without a personalized environment where students can customize how content is presented and easily track problem areas, many learners fall behind or become discouraged.

**Objectives:**

1. To develop a personalized study reader and lesson management application that allows students to read, annotate, and organize course material in a way that works for their individual learning style, with integrated reading aids like bionic reading and data-driven insights into learning patterns.
2. To allow students to create lessons manually by defining a lesson structure with custom titles and multiple content sections (panels), or automatically by uploading text files that the system splits into manageable sections.
3. To provide adjustable reading settings (bionic reading toggle, font size, line spacing, background color, theme preference, focus mode, background sound) that persist across sessions and personalize the reading experience.
4. To enable students to highlight and pin confusing or important text passages to named collections with custom color-coding so they can organize their learning challenges.
5. To allow students to create, rename, and delete custom pin collections, assign colors to each collection for visual identification, and organize pins by collection for easy browsing and review.
6. To implement full user account management with secure registration, login, and persistent storage of all student lessons, pins, settings, and collections.

### Scope

#### IN SCOPE

**Core Features:**
- User authentication (register, login, logout with email/password)
- Lesson management: manual creation (title, subtitle, unlimited panels) and automatic creation (upload .txt or .docx files with auto-splitting)
- Reading interface with text highlighting and pin-to-collection workflow
- Pinning system: select text, choose a collection, assign/view color
- Collection management: create, rename, delete custom collections; assign colors
- Default collections: "Come back to this," "Confusing," "Study this"
- Reading settings: bionic reading toggle, font size slider, line spacing slider, focus mode, background sound options, light/dark theme
- Persistent settings across sessions (stored per user account)
- Sidebar list of pins with text snippets for easy browsing
- "Jump to pin" feature: click a pin to scroll to and visually highlight it in the lesson
- Dashboard: list of user's lessons with delete/edit options, pin counts per collection

**Data Integrity:**
- Primary keys on all tables
- Foreign key relationships enforcing referential integrity
- NOT NULL constraints on required fields
- UNIQUE constraint on user email
- CHECK constraints on valid settings values (font size ranges, etc.)

#### OUT OF SCOPE / LIMITATIONS

**Features not included:**
- Mobile app (web-based only)
- Real-time collaboration or sharing with other students
- Spaced repetition reminder scheduling
- Export/print functionality for lessons and pins
- OCR or photo upload of handwritten notes or textbook pages
- Binaural beats or external music integration (only silence, brown/white noise, soft rain)
- Integration with external calendars or learning management systems (LMS)
- SMS notifications or push notifications
- Video playback or embedded media support in lessons
- Advanced AI-generated summaries or simplified explanations of confusing sections (AI analysis is optional/nice-to-have only)

---