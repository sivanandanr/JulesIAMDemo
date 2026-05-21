namespace IdentityManager.Models;

public class UserIdentity
{
    public int Id { get; set; }
    public string Username { get; set; } = string.Empty;
    public string DisplayName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public string Status { get; set; } = "Active"; // Active, Inactive, Terminated
    public string Department { get; set; } = string.Empty;
    public string JobTitle { get; set; } = string.Empty;
    public List<Role> Roles { get; set; } = new();
}
