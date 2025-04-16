# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Install dependencies from the requirements.txt file
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application code into the container
COPY . /app/

# Step 5: Set environment variables (like OPENAI_API_KEY)
ENV OPENAI_API_KEY=your_openai_api_key_here

# Step 6: Expose port 8000 (the port FastAPI runs on)
EXPOSE 8000

# Step 7: Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
