<template>
  <div class="page-detail">
    <a-back-top />

    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->
        <CardPackageInfo />
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
    <a-row type="flex" :gutter="24">
      <a-col :span="24" :md="16" class="mb-24">
        <CardPackageTable :data="table1Data" :columns="table1Columns" />
      </a-col>
    </a-row>
  </div>
</template>
<script>
import CardPackageInfo from "@/components/cards/CardPackageInfo.vue";
import CardPackageTable from "@/components/cards/CardPackageTable.vue";

// "Authors" table list of columns and their properties.
const table1Columns = [
  {
    title: "Version",
    dataIndex: "version",
    slots: { customRender: "version" },
  },
  {
    title: "Vulnerabilities",
    dataIndex: "vulnerabilities",
    slots: { customRender: "vulnerabilities" },
  },
  {
    title: "Usages",
    dataIndex: "usages",
    slots: { customRender: "usages" },
  },
  {
    title: "Date",
    dataIndex: "date",
    class: "date",
  },
];

// "Authors" table list of rows and their properties.
const table1Data = [
  {
    key: "1",
    version: { value:"4.1.1.4", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: {value: "2 vulnerabilities", href:"https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core/2.17.0"},
    usages: { value: 898, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "2",
    version: { value:"4.0.1.2", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:164, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "3",
    version: { value:"2.3.3", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:81, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "4",
    version: { value:"2.3.1", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:20, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "5",
    version: { value:"2.2.1", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:74, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "6",
    version: { value:"2.1.2", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:48, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
    {
    key: "7",
    version: { value:"4.1.1.4", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: {value: "2 vulnerabilities", href:"https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core/2.17.0"},
    usages: { value: 898, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "8",
    version: { value:"4.0.1.2", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:164, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "9",
    version: { value:"2.3.3", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:81, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "10",
    version: { value:"2.3.1", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:20, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "11",
    version: { value:"2.2.1", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:74, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
  {
    key: "12",
    version: { value:"2.1.2", href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4"},
    vulnerabilities: "",
    usages: { value:48, href:"https://mvnrepository.com/artifact/com.google.android/android/4.1.1.4/usages"},
    date: "Dec, 2015",
  },
];

export default {
  components: {
    CardPackageInfo,
    CardPackageTable,
  },

  data() {
    return {
      // Associating "Authors" table data with its corresponding property.
      table1Data: table1Data,

      // Associating "Authors" table columns with its corresponding property.
      table1Columns: table1Columns,
    };
  },
};
</script>