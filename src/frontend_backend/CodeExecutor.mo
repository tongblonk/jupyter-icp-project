// src/jupyter_icp_app/CodeExecutor.mo
actor CodeExecutor {
    stable var results: [Text] = [];

    public func saveResult(result: Text) : async () {
        results := Array.append(results, [result]);
    }

    public query func getResults() : async [Text] {
        return results;
    }
}
￼Enter
