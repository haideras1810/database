
// import { axiosInstance } from '@/http.js'

export let store = {
   state:{

        auth: {

        },
        board: {},

   },
   setBoard: (board)=>{
       store.state.board = board
       console.log(store.state.board)
   },

   setUser: (user)=>{
       store.state.auth = user
       console.log(store.state)
   }

}