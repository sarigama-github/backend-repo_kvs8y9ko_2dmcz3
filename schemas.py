"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Direction/Reflection session schema
class Reflection(BaseModel):
    """
    Reflection sessions captured from users going through the direction flow.
    Collection name: "reflection" (lowercase of class name)
    """
    feeling: str = Field(..., description="How the user is feeling right now")
    area: str = Field(..., description="Area of life needing direction (e.g., career)")
    challenge: str = Field(..., description="Main challenge or confusion")
    desired_outcome: str = Field(..., description="What clarity they hope to receive")
    action_timeline: str = Field(..., description="How soon they want to take action")

    # Generated fields
    distilled: Optional[str] = Field(None, description="A distilled interpretation of their answers")
    guidance: Optional[list[str]] = Field(default=None, description="Tailored guidance or direction suggestions")
    message: Optional[str] = Field(None, description="Short uplifting message")
    emailed_to: Optional[EmailStr] = Field(default=None, description="If sent via email, the destination address")
