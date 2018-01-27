<template>
  <button>
      {{text}}
  </button>
</template>
<script>
    export default{
        props: {
            text: String
        }
    }
</script>

<style lang="scss" scoped>
    button{
        box-sizing: border-box;
        cursor: pointer;
        font: {
            size: 24px;
            color: black;
        }
        border: {
            width: 4px;
            color: rgb(0, 0, 0);
            style: solid;
        }
        text-align: center;
        outline: none;
        margin: 0 auto;
        background-color: rgb(255, 255, 255);
        &:hover {
            border: {
                color:rgba(119, 119, 119, 0.8);
            }
            box-shadow: 1px 1px 2px rgb(119, 119, 119);
        }
        transition: border-color 0.4s, box-shadow 0.5s;
    }
</style>
