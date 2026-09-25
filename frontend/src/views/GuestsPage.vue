<script setup>
import { ref, onMounted } from 'vue'

const guests = ref([])
const loading = ref(true)

const newGuest = ref({
  name: '',
  room: '',
  room_type: 'single'
})

async function fetchGuests() {
  const res = await fetch('http://127.0.0.1:8000/guests')
  guests.value = await res.json()
  loading.value = false
}

async function addGuest() {
  await fetch('http://127.0.0.1:8000/guests', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: newGuest.value.name,
      room: parseInt(newGuest.value.room),
      room_type: newGuest.value.room_type
    })
  })
  newGuest.value = { name: '', room: '', room_type: 'single' }
  await fetchGuests()
}

async function deleteGuest(id) {
  await fetch(`http://127.0.0.1:8000/guests/${id}`, {
    method: 'DELETE'
  })
  await fetchGuests()
}

onMounted(fetchGuests)
</script>

<template>
  <div class="guests">
    <h1>🏨 Guest List</h1>

    <!-- Add guest form -->
    <div class="form">
      <h2>Add Guest</h2>
      <input v-model="newGuest.name" placeholder="Guest name" />
      <input v-model="newGuest.room" placeholder="Room number" type="number" />
      <select v-model="newGuest.room_type">
        <option value="single">Single</option>
        <option value="double">Double</option>
        <option value="suite">Suite</option>
      </select>
      <button @click="addGuest">Add Guest</button>
    </div>

    <!-- Guest list -->
    <p v-if="loading">Loading guests...</p>
    <div v-else>
      <p v-if="guests.length === 0">No guests yet.</p>
      <div v-for="guest in guests" :key="guest.id" class="guest-card">
        <h3>{{ guest.name }}</h3>
        <p>Room: {{ guest.room }} — {{ guest.room_type }}</p>
        <p>Status: {{ guest.checked_in ? 'Checked in' : 'Not checked in' }}</p>
        <button @click="deleteGuest(guest.id)" class="delete-btn">Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.guests {
  padding: 32px;
  max-width: 800px;
  margin: 0 auto;
}
.form {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
input, select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}
button {
  padding: 8px 16px;
  background: #1a1a2e;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}
button:hover { background: #00d4ff; color: #1a1a2e; }
.guest-card {
  background: #f9f9f9;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.delete-btn {
  background: #ff6b6b;
  width: fit-content;
  margin-top: 8px;
}
.delete-btn:hover { background: #ff4444; color: white; }
h3 { margin: 0; color: #1a1a2e; }
p { margin: 0; color: #555; font-size: 14px; }
</style>