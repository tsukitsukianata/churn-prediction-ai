def get_recommendations(form_data, churn_probability):
    """
    Generate business recommendations based on
    customer information and churn probability.
    """

    recommendations = []

    # Only provide recommendations for medium/high-risk customers
    if churn_probability < 0.30:
        return recommendations

    # Contract
    if form_data["Contract"] == "Month-to-month":
        recommendations.append(
            "Offer a discount or incentive to switch to a one-year or two-year contract."
        )

    # New customer
    if int(form_data["tenure"]) <= 12:
        recommendations.append(
            "Provide proactive onboarding and follow-up during the first year."
        )

    # Tech Support
    if form_data["TechSupport"] == "No":
        recommendations.append(
            "Offer a free or discounted Tech Support plan."
        )

    # Online Security
    if form_data["OnlineSecurity"] == "No":
        recommendations.append(
            "Recommend adding Online Security through a promotional bundle."
        )

    # Payment Method
    if form_data["PaymentMethod"] == "Electronic check":
        recommendations.append(
            "Encourage switching to automatic payments with a small incentive."
        )

    return recommendations