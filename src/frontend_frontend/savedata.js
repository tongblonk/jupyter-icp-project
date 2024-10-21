import { Actor, HttpAgent } from "@dfinity/agent";
import { idlFactory } from "./declarations/CodeExecutor";

// Inisialisasi Agent
const agent = new HttpAgent({ host: "https://ic0.app" });

// Inisialisasi actor untuk berkomunikasi dengan canister
const codeExecutor = Actor.createActor(idlFactory, {
    agent,
    canisterId: "your-canister-id",
});

// Simpan hasil eksekusi
async function saveExecutionResult(result) {
    await codeExecutor.saveResult(result);
}

// Contoh pemanggilan fungsi setelah eksekusi kode selesai
document.getElementById('submitCodeButton').onclick = async () => {
    const result = "Hasil eksekusi...";
    await saveExecutionResult(result);
};
