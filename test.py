from quart import Quart, request


# ************** Initialized variable **************#
app = Quart(__name__)
# QuartSchema(app)




# **************************************************************#
# **************************** User ****************************#
# **************************************************************#
# **************************************************************#
# **************************** User ****************************#
# **************************************************************#
@app.route('/')
async def index():
    l = []
    try:
        f=[]
    except Exception as e:
        print(e)
        print("System error, please contact the author.")
    return {"msg": "Welcome to the Wordle game. Now listing all users in database.",
            "number_of_users": len(l), "data": l}


if __name__ == '__main__':
    try:


        app.run(debug=True)
    except Exception as e:
        print(e)
        print("The system initialization failed, please contact the author.")
