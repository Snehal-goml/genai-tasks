# VYRA - Agentic AI Assistant

## Overview
VYRA has been refactored into a proper agentic AI architecture with OpenAI-style orchestration, multi-step reasoning, tool use, and self-reflection capabilities.

## Architecture

### Agentic Pipeline
The agent now follows a structured 4-phase pipeline:

1. **THINK Phase** - Analyzes user input and prepares context
2. **EXECUTE Phase** - Uses tools (style router, context manager)
3. **RESPOND Phase** - Generates the actual response
4. **REFLECT Phase** - Self-evaluates response quality

### Core Components

#### 1. Data Structures
- `AgentState` - Tracks current agent state (IDLE, THINKING, EXECUTING, etc.)
- `Message` - Structured message format with metadata
- `ReasoningStep` - Individual steps in agent reasoning chain
- `AgentResponse` - Comprehensive response with reasoning, tools, and reflection

#### 2. Agentic Tools
- **StyleRouterTool** - Determines appropriate speaking style (SRK/Ranveer)
- **ContextManagerTool** - Manages conversation history and context window
- **ReflectionTool** - Self-evaluates response quality

#### 3. Agent Class (VyraAgent)
- Multi-step reasoning with explicit state management
- Tool-based execution
- Memory management (50 message window)
- Reasoning chain tracking
- Agent status reporting

## New Features

### 1. Agentic UI Components
- **Agent Status Display** - Real-time agent state in sidebar
  - 🔄 Analyzing...
  - ⚡ Using tools...
  - ✨ Crafting response...
  - 🤔 Reflecting...
  - ✅ Ready
- **Agent Info Panel** - Shows reasoning steps, memory size, tools available
- **Reasoning Chain Visualization** - Expandable section showing agent's thought process
- **Tool Usage Display** - Shows which tools were used during response generation
- **Self-Reflection Display** - Agent's own evaluation of its response

### 2. Agentic Features Toggle
Users can toggle visibility of:
- Agent reasoning steps
- Tool usage
- Self-reflection

### 3. Enhanced Chat Header
- Message count metric
- Current style indicator with emoji (🎭 SRK or 🔥 Ranveer)

### 4. Improved Edit & Regenerate
- Edit prompt with "Save & Regenerate" button
- Automatically generates new response based on edited prompt
- Removes subsequent messages after edit
- Shows thinking indicator during regeneration

### 5. Agent State Management
- Proper state tracking throughout conversation
- Agent reset on new chat
- Error state handling
- Memory management

## Style Preservation

### SRK Style (🎭 Calm Witty Mode)
- Thoughtful and philosophical
- Clever wit and dry sarcasm
- Meaningful advice
- Polished and warm
- NOT flirty

### Ranveer Style (🔥 High-Energy Mode)
- Energetic and bold
- Playful and expressive
- Strong motivation
- Occasional emojis (🔥 😂 ⚡ 😎)
- Confident and humorous

## Technical Improvements

### Code Quality
- Type hints throughout
- Dataclasses for structured data
- Proper separation of concerns
- Agentic design patterns
- Tool-based architecture
- State machine implementation

### Performance
- Context windowing (last 10 messages)
- Memory management (50 message limit)
- Efficient tool execution
- Error handling and recovery

## Usage

### Basic Chat
1. Type message in chat input
2. VYRA analyzes input using agentic pipeline
3. Selects appropriate style (SRK or Ranveer)
4. Generates response with reasoning
5. Optionally reflects on response quality

### Edit & Regenerate
1. Click "✏️ Edit prompt" on any user message
2. Modify the prompt
3. Click "💾 Save & Regenerate"
4. VYRA regenerates response based on edited prompt

### Agent Features
1. Toggle reasoning display in sidebar
2. Toggle tool usage display
3. Toggle self-reflection display
4. View agent state and metrics

## File Structure

```
VYRA/
├── agent.py          # Agentic AI core with tools and reasoning
├── app.py           # Agentic UI with state management
├── personalities.py # SRK and Ranveer style prompts
├── styles.py        # CSS styling
└── requirements.txt # Dependencies
```

## Dependencies
- streamlit
- requests
- dataclasses (Python 3.7+)
- typing (Python 3.5+)

## Running the App

```bash
streamlit run app.py
```

## Future Enhancements

Potential additions:
1. Multi-agent orchestration (specialized agents)
2. External tool integrations (web search, code execution)
3. Memory persistence across sessions
4. Response streaming for real-time display
5. Agent-to-agent conversations
6. Custom agent personalities
7. Learning from user feedback
8. Multi-modal capabilities (images, voice)

## Notes

- Requires Ollama running with llama3.2:3b model
- Agentic features can be toggled on/off
- All original features preserved (chat history, edit, delete)
- Maintains SRK and Ranveer Singh speaking styles
- No actual celebrity impersonation - fictional inspired styles