namespace IdentityManager.Models;

public class Entitlement
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Type { get; set; } = string.Empty; // AD Group, Folder Access, etc.
    public string Description { get; set; } = string.Empty;
}
