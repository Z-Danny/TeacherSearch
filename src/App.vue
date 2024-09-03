<template>
	<div class="app img10">
    <header >
      <!-- 头部导航栏 -->
      <div class="header pcshow nosyheader">
        <div class="flex-between align-center">
          <img src="@/assets/uestc_header.png" alt="" class="logo"/>
            <div class="nav">
              <a href="/index.html" class="">首页</a>
              <a href="/schools.html" class="">学院列表</a>
              <a href="/discipline.html" class="">学科列表</a>
            </div>
        </div>
      </div>
      <!-- 电子科技的图片 -->
      <div class="xkt tc">
        <img src="@/assets/topbjtp.jpg" alt="" class="background-image">
      </div>

      <h1>教 师 查 询 / Teacher Search</h1>

			<!-- 筛选块 -->

      <div class="filter-buttons">
        <ul>
          <!-- 按学院筛选 -->
          <li class="flex-start align-start pt15 pb10">
            <span class="xytl b lan f16">学院</span>
            <div class="xytr flex-between align-center">
              <div class="xyselect">
                <div class="flex-start flex-wrap school-lay">
                    <a href="javascript:void(0)" @click="toggleSchoolList" >全部学院</a>
                    <div v-if="showSchoolList" class="school-list" ref="schoolList">
                      <a v-for="school in schoolList" :key="school.name" @click="selectSchool(school.name)">
                        <span>{{ school.name }}</span>
                      </a>
                    </div>  
                  </div>
                </div>
                <div class="dyym2 flex-between align-center">
                  <input type="text" class="dyym2_input" name="sea" id="sea" maxlength="20" value="" placeholder="请输入教师姓名">
                  <button class="dyym2_btn flex-column align-center">搜索</button>
                </div>

            </div>
          </li> 

          <!-- 按职称筛选 -->
          <li class="flex-start align-start pt15 pb10">
            <span class="xytl b lan f16">职称</span>
            <div class="xytr rytxt flex-start flex-wrap box-tit">
              <button 
                :class="{ active: selectedGroup === '' }"
                @click="resetFilter">
                全部
              </button>
              <button  v-for="group in courseGroups" 
            :key="group"
            :class="{ active: selectedGroup === group }"
            @click="filterByGroup(group)">
            {{ group }}
          </button>
            </div>
          </li> 
          <!-- 按姓氏字母筛选 -->
          <li class="flex-start align-start pt15 pb10">
            <span class="xytl b lan f16">按姓氏字母</span>
            <div class="xytr rytxt flex-start flex-wrap box-tit">
              <button 
                :class="{ active: selectedGroup === '' }"
                @click="resetFilter">
                全部
              </button>
              <button  v-for="group in courseGroups" 
            :key="group"
            :class="{ active: selectedGroup === group }"
            @click="filterByGroup(group)">
            {{ group }}
          </button>
            </div>
          </li> 
				
           
          

        </ul>
        
				
			</div>



		</header>
		<main>
    <div class="xycx pr xycx-box">
			<div class="cards" v-if="teachers.length > 0">
				<Card 
					v-for="teacher in filteredTeachers" 
					:key="teacher.Name"
					:teacher = "teacher" />
			</div>
			<div class="no-results" v-else>
				<h3>没有找到教师信息...</h3>
			</div>
    </div>
		</main>
		
	</div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Card from './components/Card.vue';

/* 导入 Card 组件 */
export default {
  components: { Card },
  setup() {
    const teachers = ref([]);
	const filteredTeachers = ref([]);
	const selectedGroup = ref("");
	const courseGroups = ref(["理论与方法类课程群", "技术与应用类课程群", "创作与设计类课程群", "美育课程群"]); // 替换为实际课程群

  /* 从 API 获取教师信息 */
	const fetchTeachers = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/teachers');
        teachers.value = response.data;
		filteredTeachers.value = response.data; // 初始化时显示所有教师
      } catch (error) {
        console.error("Error fetching teachers:", error);
      }
    }
    /* 根据课程群筛选教师 */
	const filterByGroup = (group) => {
			selectedGroup.value = group;
			console.log("Selected Group:", group);
			filteredTeachers.value = teachers.value.filter(teacher => teacher.Department === group);
			console.log("Filtered Teachers:", filteredTeachers.value);
		};

	const resetFilter = () => {
			selectedGroup.value = "";
			filteredTeachers.value = teachers.value;
		};

    onMounted(() => {
      fetchTeachers();
    });

    return {
      teachers,
	filteredTeachers,
	selectedGroup,
	courseGroups,
	filterByGroup,
	resetFilter,
    };
  },
  data() 
  {
    return {
      showSchoolList: false,
      schoolList:[{ name: '航空学院' },
        { name: '化学学院' },
        { name: '物理学院' },
        { name: '计算机学院' },
        { name: '生物学院' }],
    }
  },
  // 新增方法
  methods: 
  {
    toggleSchoolList() {
      this.showSchoolList = !this.showSchoolList;
      if (this.showSchoolList) {
        this.$nextTick(() => {
          this.positionList();
        });}
    },

    selectSchool(schoolName) {
      this.showSchoolList = false;
      // 这里可以处理选中学院后的逻辑
      console.log(`Selected school: ${schoolName}`);
    },

    positionList() {
      const trigger = this.$el.querySelector('a[href="javascript:void(0)"]');
      const list = this.$refs.schoolList;
      list.style.position = 'absolute';
      list.style.top = `${trigger.offsetTop + trigger.offsetHeight}px`;
      list.style.left = `${trigger.offsetLeft}px`;
      list.style.width = `${trigger.offsetWidth}px`;
    }
  }
}
</script>

// 元素样式与美化
<style scoped lang="scss">
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0px;
}

header {
  text-align: center;
  margin-bottom: 20px;

  h1 {
    /* 为标题添加样式 */
  font-size: 2.5rem;
  margin: 1rem 0;
  font-weight: 700;
  color: #2c3e50;
  text-transform: uppercase; 
  letter-spacing: 0.05rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); 
  border-bottom: 2px solid #3498db; 
  padding-bottom: 0.5rem;        
  line-height: 1.2;              
}


.filter-buttons {
  display: flex;
  justify-content: flex-start;     /* 左对齐排列按钮 */
  margin-top: 1rem;
  gap: 1.5rem;                /* 增加按钮之间的间距 */
}

.filter-buttons button {
  // background-color: #3498db;
  // color: white;
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  border: none;
  border-radius: 7px;
  padding: 0.5rem 1rem; 
  font-size: 1rem;
  //font-weight: 600;  /*字体粗细*/
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease; 
  box-shadow: 0 4px 1px rgba(0, 0, 0, 0.1); 
}


.filter-buttons button:hover {
/* 按钮悬浮效果 */
  background-color: #2980b9; 
  transform: translateY(-2px); 
}



.filter-buttons button:active {
  background-color: #1f6395;
  transform: translateY(0);
}

.filter-buttons button.active {
  // background-color: #2c3e50;
  background-color:#1f6395; 
}

.filter-buttons button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.4); 
}

}

main {
  /* 主要内容区域样式 */
  width: 100%;
  display: flex;
  justify-content: center;
  
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    max-width: 1200px;
    width: 100%;
  }

  .no-results {
    text-align: center;
    color: gray;
  }
}
</style>
