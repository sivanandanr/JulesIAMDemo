namespace IdentityManager.Models;

public class Application
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public int ConnectorId { get; set; }
    public bool IsTrustedSource { get; set; } = false;
    public List<Entitlement> Entitlements { get; set; } = new();
}
