<script setup>
import { ref, onMounted } from 'vue'

const reservations = ref([])
const loading = ref(true)
const API = 'https://fullstack-journey-production.up.railway.app'

const newReservation = ref({
  guest_id: '',
  check_in: '',
  check_out: '',
  room: ''
})

async function fetchReservations() {
  const res = await fetch(`${API}/reservations`)
  reservations.value = await res.json()
  loading.value = false
}

async function addReservation() {
  await fetch(`${API}/reservations`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      guest_id: parseInt(newReservation.value.guest_id),
      check_in: newReservation.value.check_in,
      check_out: newReservation.value.check_out,
      room: parseInt(newReservation.value.room)
    })
  })
  newReservation.value = { guest_id: '', check_in: '', check_out: '', room: '' }
  await fetchReservations()
}

onMounted(fetchReservations)
</script>

<template>
  <div class="reservations">
    <h1>📅 Reservations</h1>
    <div class="form">
      <h2>New Reservation</h2>
      <input v-model="newReservation.guest_id" placeholder="Guest ID" type="number" />
      <input v-model="newReservation.room" placeholder="Room number" type="number" />
      <input v-model="newReservation.check_in" type="date" />
      <input v-model="newReservation.check_out" type="date" />
      <button @click="addReservation">Add Reservation</button>
    </div>
    <p v-if="loading">Loading...</p>
    <div v-else>
      <p v-if="reservations.length === 0">No reservations yet.</p>
      <div v-for="r in reservations" :key="r.id" class="reservation-card">
        <h3>Reservation #{{ r.id }}</h3>
        <p>Guest ID: {{ r.guest_id }}</p>
        <p>Room: {{ r.room }}</p>
        <p>Check in: {{ r.check_in }}</p>
        <p>Check out: {{ r.check_out }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.reservations { padding: 32px; max-width: 800px; margin: 0 auto; }
.form { background: #f5f5f5; padding: 20px; border-radius: 8px; margin-bottom: 24px; display: flex; flex-direction: column; gap: 10px; }
input { padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; }
button { padding: 8px 16px; background: #1a1a2e; color: white; border: none; border-radius: 6px; cursor: pointer; }
button:hover { background: #00d4ff; color: #1a1a2e; }
.reservation-card { background: #f9f9f9; border-radius: 8px; padding: 16px; margin-bottom: 12px; }
h3 { margin: 0 0 8px; color: #1a1a2e; }
p { margin: 4px 0; color: #555; font-size: 14px; }
</style>