"""Stripe integration helpers."""
from __future__ import annotations

from typing import Dict

import stripe

from .config import settings

stripe.api_key = settings.stripe_api_key


def create_subscription(customer_id: str, price_id: str) -> Dict[str, str]:
    """Create a recurring subscription for a user."""
    subscription = stripe.Subscription.create(customer=customer_id, items=[{"price": price_id}])
    return {"id": subscription.id, "status": subscription.status}


def create_payout(amount_cents: int, currency: str = "usd") -> Dict[str, str]:
    """Send a payout to the connected account."""
    payout = stripe.Payout.create(amount=amount_cents, currency=currency)
    return {"id": payout.id, "status": payout.status}


def list_payments(customer_id: str) -> Dict[str, str]:
    """List payment intents for a customer."""
    payments = stripe.PaymentIntent.list(customer=customer_id, limit=10)
    return {"payment_intents": [p.id for p in payments.data]}
