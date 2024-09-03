from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# 允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 读取 CSV 文件
df = pd.read_csv('src/assets/professors_data.csv')

@app.get("/teachers")
def get_teachers():
    return df.to_dict(orient='records')

@app.get("/teacher/{name}")
def get_teacher(name: str):
    teacher = df[df['Name'] == name]
    if not teacher.empty:
        return teacher.to_dict(orient='records')[0]
    return {"error": "Teacher not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
