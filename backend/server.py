from fastapi import FastAPI
from copilotkit.integrations.fastapi import add_fastapi_endpoint
from copilotkit import CopilotKitRemoteEndpoint, Action as CopilotAction

app = FastAPI()

# Define your backend action
async def fetch_name_for_user_id(userId: str):
    # Simulated database fetch
    return {"name": "User_" + userId}

# Dummy action for demonstration purposes
action = CopilotAction(
    name="fetchNameForUserId",
    description="Fetches user name for a given ID.",
    parameters=[
        {
            "name": "userId",
            "type": "string",
            "description": "The ID of the user to fetch data for.",
            "required": True,
        }
    ],
    handler=fetch_name_for_user_id
)

# Initialize the CopilotKit SDK
sdk = CopilotKitRemoteEndpoint(actions=[action])

# Add the CopilotKit endpoint to your FastAPI app
add_fastapi_endpoint(app, sdk, "/copilotkit_remote")

# Running the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
