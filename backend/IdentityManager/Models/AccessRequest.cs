namespace IdentityManager.Models;

public class AccessRequest
{
    public int Id { get; set; }
    public int RequesterId { get; set; }
    public string RequesterName { get; set; } = string.Empty;
    public int IdentityId { get; set; }
    public string IdentityName { get; set; } = string.Empty;
    public string RequestType { get; set; } = "Role"; // Role, Entitlement
    public int TargetId { get; set; }
    public string TargetName { get; set; } = string.Empty;
    public string Status { get; set; } = "Pending"; // Pending, Approved, Rejected, Completed
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public string Comments { get; set; } = string.Empty;
    public List<WorkflowStep> WorkflowSteps { get; set; } = new();
}
