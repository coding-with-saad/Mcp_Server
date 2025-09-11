- [1. Fundamental Prompting Techniques](#1-fundamental-prompting-techniques)
  - [1.1. Zero-Shot Prompting](#11-zero-shot-prompting)
  - [1.2. One-Shot Prompting](#12-one-shot-prompting)
  - [1.3. Few-Shot Prompting](#13-few-shot-prompting)
  - [1.4. System Prompting](#14-system-prompting)
  - [1.5. Role Prompting](#15-role-prompting)
  - [1.6. Contextual Prompting](#16-contextual-prompting)
- [2. Advanced Prompting Strategies](#2-advanced-prompting-strategies)
  - [2.1. Chain of Thought (CoT) Prompting](#21-chain-of-thought-cot-prompting)
  - [2.2. Self-Consistency](#22-self-consistency)
  - [2.3. Step-Back Prompting](#23-step-back-prompting)
  - [2.4. ReAct (Reasoning + Acting)](#24-react-reasoning--acting)
  - [2.5. Tree of Thoughts (ToT)](#25-tree-of-thoughts-tot)
- [3. Best Practices for Effective Prompts](#3-best-practices-for-effective-prompts)
  - [3.1. Be Specific and Clear](#31-be-specific-and-clear)
  - [3.2. Use Action Verbs](#32-use-action-verbs)
  - [3.3. Provide Examples When Possible](#33-provide-examples-when-possible)
  - [3.4. Structure Your Prompts](#34-structure-your-prompts)
  - [3.5. Use Instructions Over Constraints](#35-use-instructions-over-constraints)
  - [3.6. Control Output Format](#36-control-output-format)
  - [3.7. Use Variables for Reusability](#37-use-variables-for-reusability)

## 1. Fundamental Prompting Techniques

### 1.1. Zero-Shot Prompting

The simplest approach—just ask directly without examples.

**Example:**
```
Classify this movie review as positive, negative, or neutral:
"The film was visually stunning but the plot felt rushed."
```

**When to use:**
- Simple, well-defined tasks
- When the model has clear knowledge of the domain
- Quick one-off requests

### 1.2. One-Shot Prompting

Provide a single example to guide the response format.

**Example:**
```
Translate English to French:

English: "Hello, how are you?"
French: "Bonjour, comment allez-vous?"

English: "Where is the library?"
French:
```

### 1.3. Few-Shot Prompting

Provide multiple examples to establish a clear pattern.

**Example:**
```
Convert customer feedback to structured data:

Feedback: "Great service, but food was cold"
JSON: {"service": "positive", "food": "negative", "overall": "mixed"}

Feedback: "Amazing experience, will definitely return"
JSON: {"service": "positive", "food": "positive", "overall": "positive"}

Feedback: "Terrible food and rude staff"
JSON:
```

**Best practices:**
- Use 3-5 examples for most tasks
- Include diverse examples
- Mix up the classes in classification tasks
- Ensure examples are high-quality and consistent

### 1.4. System Prompting

Set overall context and behavior guidelines.

**Example:**
```
You are a helpful travel guide. Provide practical, accurate information about destinations. Always include:
- Key attractions
- Local customs to be aware of
- Budget considerations
- Best time to visit

User: Tell me about visiting Tokyo.
```

### 1.5. Role Prompting

Assign a specific character or expertise to the AI.

**Example:**
```
Act as an experienced software architect. I need help designing a scalable web application for 1 million users. What architecture patterns should I consider?
```

**Effective roles:**
- Subject matter expert (doctor, lawyer, teacher)
- Creative roles (writer, designer, poet)
- Analytical roles (data analyst, consultant)
- Communication styles (friendly tutor, formal advisor)

### 1.6. Contextual Prompting

Provide specific background information relevant to the task.

**Example:**
```
Context: You're writing for a tech blog aimed at beginners who have never coded before.

Write a 200-word explanation of what an API is, using simple language and practical examples.
```

## 2. Advanced Prompting Strategies

### 2.1. Chain of Thought (CoT) Prompting

Encourage step-by-step reasoning for complex problems.

**Example:**
```
Solve this step by step:
If I was 6 when my sister was half my age, how old is my sister when I'm 40?

Let me think through this step by step:
```

**When to use:**
- Math problems
- Logical reasoning
- Complex analysis
- Multi-step processes

**Best practices:**
- Use "Let's think step by step" or similar phrases
- Set temperature to 0 for consistent reasoning
- Extract final answers separately from reasoning

### 2.2. Self-Consistency

Generate multiple reasoning paths and select the most common answer.

**Process:**
1. Ask the same question multiple times with different phrasings
2. Compare the answers
3. Choose the most frequently occurring result

**Example:**
```
Question: If a store offers a 20% discount on a $50 item, what is the final price?

Generate 3 different reasoning paths for this question and select the most consistent answer.

Path 1: To find the final price, calculate the discount: 20% of $50 is 0.20 × 50 = $10. Subtract this from the original price: $50 - $10 = $40. The final price is $40.

Path 2: A 20% discount means paying 80% of the original price. So, 80% of $50 is 0.80 × 50 = $40. Therefore, the final price is $40.

Path 3: Compute the discount amount: 20% = 0.20, so 0.20 × $50 = $10 off. The original price is $50, so after the discount, it’s $50 - $10 = $40. The final price is $40.

Most common answer: $40
```

**Explanation of Concept:**
Self-Consistency involves generating multiple answers to the same question using varied reasoning approaches to ensure reliability. By comparing the results, you select the most frequent or consistent outcome, reducing the chance of errors from a single flawed reasoning path. This method leverages the model's ability to approach the problem from different angles, increasing confidence in the final answer when all paths converge, as seen here with the consistent result of $40.

### 2.3. Step-Back Prompting

Ask a more general question first, then use that context for the specific question.

**Example 1:**
```
First, what are the key principles of good user interface design?

[Get response]

Now, using those principles, redesign this mobile app's login screen: [description]
```

**Example 2:**
Question: How should I optimize the loading speed of my e-commerce website?
```
Step 1: First, what are the key factors that generally affect website loading speed?

Response: Key factors include:
- Server response time (hosting quality, server location)
- Image and asset optimization (file size, compression)
- Code efficiency (minifying CSS/JavaScript, reducing HTTP requests)
- Caching strategies (browser caching, CDNs)
- Third-party scripts (ads, analytics)

Step 2: Using these factors, provide specific recommendations to optimize the loading speed of an e-commerce website with heavy product images and multiple third-party plugins.

Response:
1. **Server Optimization**: Choose a reliable hosting provider with servers close to your audience. Enable server-side caching (e.g., Redis or Varnish).
2. **Image Optimization**: Compress product images using formats like WebP. Implement lazy loading to defer off-screen images.
3. **Code Efficiency**: Minify CSS and JavaScript files. Combine small files to reduce HTTP requests.
4. **Caching**: Use a Content Delivery Network (CDN) like Cloudflare to cache static content globally. Set browser cache headers for repeat visitors.
5. **Third-Party Plugins**: Audit and remove unnecessary plugins. Asynchronously load scripts for analytics or ads to avoid blocking page rendering.

```

**Explanation of Concept:**
Step-Back Prompting involves first asking a broader, foundational question to establish key principles or context before tackling the specific task. This approach ensures the model grounds its response in general knowledge (e.g., factors affecting website speed) before applying it to the specific problem (e-commerce site optimization). By breaking the task into two steps, the model produces more informed and structured recommendations, reducing the risk of overlooking critical factors.


### 2.4. ReAct (Reasoning + Acting)

Combine reasoning with tool use or actions.

**Example 1:**
```
I need to find out how many children the members of Metallica have in total.

Thought: I need to find information about each band member and their children.
Action: Search for "Metallica band members"
Observation: [results]
Thought: Now I need to search for each member individually...
```

**Example 2:**
```
Question: What is the current population of Tokyo, and how does it compare to New York City?

Thought: I need to find the current population of Tokyo and New York City to compare them. I should start by searching for the latest population data for Tokyo.

Action: web_search
<parameter name="query">current population of Tokyo 2025</parameter

Observation: [Assume tool response: According to recent estimates, Tokyo's population in 2025 is approximately 37.4 million in the metropolitan area.]

Thought: Now I have Tokyo's population. Next, I need the population for New York City.

Action: web_search
<parameter name="query">current population of New York City 2025</parameter

Observation: [Assume tool response: New York City's metropolitan area population in 2025 is estimated at about 23.6 million.]

Thought: With both figures, I can compare them. Tokyo has a larger population than New York City by about 13.8 million people.

Final Answer: Tokyo's population is approximately 37.4 million, compared to New York City's 23.6 million, making Tokyo significantly larger.

```

**Explanation of Concept:**
ReAct (Reasoning + Acting) is a prompting strategy that interleaves reasoning steps (Thoughts) with actions (tool calls or external queries) to solve complex problems iteratively. Each cycle includes a Thought (planning the next step), an Action (executing a tool or search), and an Observation (processing the result). This loop continues until the question is resolved, allowing the model to dynamically gather information and refine its approach. It's particularly useful for tasks requiring real-time data or multi-step verification, as demonstrated by sequentially fetching and comparing population data.

### 2.5. Tree of Thoughts (ToT)

Explore multiple reasoning branches simultaneously for complex problems.

**When to use:**
- Creative problem solving
- Strategic planning
- Complex decision-making
- Tasks requiring exploration of alternatives


**Example:**

Question: What is the best marketing strategy for launching a new eco-friendly clothing brand targeting young adults?

Task: Explore multiple strategic approaches, evaluate them, and select the best one.

**Branch 1: Social Media Campaign**
Thought: Young adults are active on platforms like Instagram and TikTok. A campaign using influencers could build brand awareness.
Exploration:
- Pros: High engagement, visually appealing for clothing, cost-effective with micro-influencers.
- Cons: Risk of inauthentic partnerships, oversaturation in influencer marketing.
Evaluation: Strong for visibility but needs unique content to stand out. Score: 8/10.

**Branch 2: Sustainable Pop-Up Events**
Thought: Hosting pop-up shops at eco-conscious festivals or college campuses could create direct engagement.
Exploration:
- Pros: Hands-on experience with products, builds community, aligns with eco-friendly values.
- Cons: High logistical costs, limited geographic reach.
Evaluation: Great for brand authenticity but resource-intensive. Score: 7/10.

**Branch 3: Collaborative Partnerships**
Thought: Partnering with eco-friendly brands (e.g., sustainable accessories) could cross-promote to aligned audiences.
Exploration:
- Pros: Expands reach via partner networks, reinforces eco-mission.
- Cons: Complex coordination, potential brand dilution.
Evaluation: Effective for niche targeting but requires careful partner selection. Score: 7.5/10.

**Synthesis**: Combine a social media campaign (Branch 1) with selective pop-up events (Branch 2) for maximum impact. Use partnerships (Branch 3) to amplify reach at events.

Final Strategy: Launch with a TikTok influencer campaign showcasing eco-friendly clothing, paired with pop-up shops at green festivals to engage young adults directly. Collaborate with a sustainable accessory brand to co-promote at events.


**Explanation of Concept:**
Tree of Thoughts (ToT) involves generating multiple reasoning branches to explore different solutions to a problem, evaluating each, and synthesizing the best ideas into a final answer. Each branch represents a distinct approach, which is explored, assessed for pros and cons, and scored. This method is ideal for complex, open-ended tasks like strategic planning, as it encourages creative exploration and systematic comparison, as shown in the marketing strategy example above.


## 3. Best Practices for Effective Prompts

### 3.1. Be Specific and Clear

**Bad:**
```
Write about dogs.
```

**Good:**
```
Write a 300-word informative article about the health benefits of owning a dog, focusing on mental health, physical activity, and social connections. Use a friendly, accessible tone for general readers.
```

### 3.2. Use Action Verbs

Be explicit about what you want the AI to do:
- Analyze, Compare, Create, Describe, Evaluate
- Extract, Generate, List, Rank, Summarize
- Translate, Write, Explain, Classify

### 3.3. Provide Examples When Possible

Examples are the most powerful way to communicate your expectations.

### 3.4. Structure Your Prompts

Use clear formatting:
```
Task: [What you want done]
Context: [Background information]
Format: [How you want the output structured]
Example: [Sample of desired output]
```

### 3.5. Use Instructions Over Constraints

**Better:**
```
Write a professional email summarizing the key points from our meeting.
```

**Avoid:**
```
Write an email but don't make it too long or too informal or too detailed.
```

### 3.6. Control Output Format

Specify exactly how you want the response structured:
```
Return your answer as a JSON object with the following structure:
{
  "main_idea": "string",
  "supporting_points": ["string", "string"],
  "confidence_level": "high/medium/low"
}
```

### 3.7. Use Variables for Reusability

```
Role: You are a {expertise} expert
Task: Analyze the {document_type} and provide recommendations for {target_audience}
Context: This is for a {industry} company with {company_size} employees
```
