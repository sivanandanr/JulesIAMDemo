namespace IdentityManager.Models;

public class WorkflowStep
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty; // e.g. Manager Approval, Security Review
    public string Approver { get; set; } = string.Empty;
    public string Status { get; set; } = "Pending"; // Pending, Approved, Rejected
    public DateTime? ActionedAt { get; set; }
}
