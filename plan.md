# Personal Accountability Bot - PRD

## 1. Product Overview
The Personal Accountability Bot is a digital assistant designed to help users maintain focus on their goals and daily tasks through regular check-ins via WhatsApp. It aims to provide personalized support and encouragement throughout the day, leveraging past interactions to offer relevant and timely advice.

## 2. Objectives
- Improve user's daily productivity and goal achievement with accountability
- Simulate a future version of themselves who has achieved their goals
- Provide consistent daily check-ins and reminders
- Offer personalized support based on user's history and context
- Maintain an ongoing record of user's progress and challenges

## 3. Target User
- Individuals seeking to improve personal accountability and goal achievement
- Initially designed for a single user (the product owner)

## 4. Key Features

### 4.1 Daily Check-ins
- Morning check-in (7:30 AM - 8:30 AM)
- Lunchtime check-in
- Evening reflection

### 4.2 Contextual Conversations
- Discuss sleep quality and daily outlook
- Review task progress and eating habits
- Reflect on daily achievements and challenges

### 4.3 Personalized Interactions
- Utilize recent conversation history (last 4 days)
- Incorporate significant past events
- Weight recent interactions more heavily

### 4.4 Data Management
- Store daily conversation summaries
- Maintain full transcripts for the past 4 days
- Implement RAG (Retrieval-Augmented Generation) for contextual responses

## 5. User Journey

1. Morning Check-in (7:30 AM - 8:30 AM)
   - User receives a WhatsApp message
   - Bot initiates a conversation about sleep quality and daily outlook
   - Bot provides encouragement with examples of how he succeeded on a day like this

2. Lunchtime Check-in
   - Bot sends a message to check on mindset and progress
   - Inquire about user's eating habits
   - Offer support or adjustments to daily plan if needed

3. Evening Reflection (After dinner time)
   - Bot prompts user to reflect on the day's achievements and challenges
   - Reinforce user's goals and provide strategies to minimize distractions
   - Capture key insights for future reference

## 6. Technical Specifications

### 6.1 Tech Stack
- Frontend/UX: WhatsApp
- Backend: Python
- Messaging: Twilio API
- Database: Supabase
- Deployment: Vercel (with scheduled functions)
- AI/NLP: Claude 3.5 Sonnet

### 6.2 Data Model
- Users Table: user_id, phone_number, time_zone, preferences
- Conversations Table: conversation_id, user_id, timestamp, type (morning/lunch/evening), summary
- Transcripts Table: transcript_id, conversation_id, full_text (limited to last 4 days)
- Goals Table: goal_id, user_id, description, target_date, status

### 6.3 Key Functions
- Message scheduling with some randomization
- AI Natural language processing for conversation understanding
- AI Text generation for responses
- Summary generation for conversation storage
- RAG implementation for contextual responses
- Twilio integration for WhatsApp messaging

## 7. Performance Metrics
- Daily engagement rate
- User-reported productivity improvements
- Goal achievement rate
- System uptime and message delivery success rate

## 8. Future Enhancements
- Integration with task management systems
- Multi-user support
- Voice message option
- Customizable check-in schedules
- Integration with wearables for sleep and activity data

## 9. Development Phases

### Phase 1: MVP (Current Focus)
- Implement basic daily check-ins (morning, lunch, evening)
- Set up Twilio for WhatsApp messaging
- Develop conversation flow logic
- Implement basic data storage in Supabase

### Phase 2: Enhanced Personalization
- Implement RAG for contextual conversations
- Develop summary generation for conversations
- Enhance conversation logic with NLP capabilities

### Phase 3: Advanced Features
- Implement task list functionality
- Develop more sophisticated personalization algorithms
- Explore integration with other productivity tools

## 10. Success Criteria
- Consistent daily engagement from the user
- Improved goal achievement rates
- Positive user feedback on bot's helpfulness
- Successful storage and retrieval of conversation history

This PRD will serve as a living document, guiding the development process and evolving as we gather more insights and user feedback.