"""
This class helps you write prompts faster and it follows good prompt engineering practices.

notes:
A prompt is made up up contexts and instructions, that are both delimited. 
So, when writing the prompt we specify the delimits too, on top of the contexts and instructions.

<table1>
...
<table1>

<table2>
...
<table2>

<instructions>
- step 1
- step 2
<instructions>
"""

class PromptDesigner():
    
    def design(self, instructions:list, instructions_delimiter = "instructions", contexts: list = [], context_delimiters: list = []) -> str:
        
        prompt = ""
        
        if len(contexts) != 0:
            prompt = self._delimit(contexts, context_delimiters)

        prompt += self._delimit(instructions, instructions_delimiter)
        
        return prompt
         
            
    def _delimit(self, content: list, delimiters):
        assert isinstance(content, list)

        prompt = ""

        if isinstance(delimiters, list):
            assert len(content) == len(delimiters)
            for c, d in zip(content, delimiters): 
                prompt += f"<{d}>\n{c}\n<{d}>\n\n"

        elif isinstance(delimiters, str):
            prompt += f"<{delimiters}>\n"
            for c in content:
                prompt += f"- {c}\n"
            prompt += f"<{delimiters}>\n\n"
                
        return prompt

