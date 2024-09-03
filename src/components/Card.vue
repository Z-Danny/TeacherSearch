<template>
  <dev>
    <li class="teacher">
      <a :href="teacher.Url" target="_blank">
        <img :src="'src/assets/photos/' + teacher.Name + '.jpg'" alt="teacher" />
        <h3>{{ teacher.Name }}</h3>
        <p>{{ teacher.Department }}</p>
        <!-- <p>{{ teacher.Email }}</p> -->
      </a>    
    </li>
  </dev>
  </template>

<script>
export default {
  name: 'TeacherCard',
  props: {
    teacher: Object
  }
}
</script>


//元素样式与美化
<style scoped lang="scss">
.teacher {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background-color: rgb(255, 255, 255);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
 
  &:hover {
    /* 鼠标悬浮效果 */
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    text-decoration: underline;
    
  }

  img {
    width: 200px;  /* 固定宽度 */
    height: 240px; /* 固定高度 */
    border-radius: 10%; /* 圆形图片 */
    object-fit: cover;  /* 图片适应容器 */
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  h3 {
    font-size: 1.2rem;
    margin: 10px 0;
    text-align: center;
  }

  p {
    font-size: 1rem;
    color: #666;
    text-align: center;
    margin: 5px 0;
  }
}
</style>

