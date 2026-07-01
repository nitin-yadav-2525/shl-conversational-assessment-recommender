def build_response(
    reply,
    recommendations=None,
    end=False
):

    return {

        "reply": reply,

        "recommendations": recommendations,

        "end_of_conversation": end

    }